"""Chat message handler: Ask AI mode only → intent / LLM with KB + catalog/site."""

from __future__ import annotations

import logging

from aiogram import F, Router
from aiogram.types import Message

from src.ai.client import AIClient, AIClientError
from src.ai.persona import (
    SUPPORT_HANDLE,
    append_sales_if_needed,
    build_system_prompt,
    download_or_site_fallback,
    format_facts_from_meta,
    join_context_blocks,
    looks_incomplete_reply,
    looks_like_reasoning_leak,
    sanitize_reply_links,
    strip_reasoning_leak,
    wants_contact_links,
    wants_sales_nudge,
)
from src.access import AdminAccess
from src.config import Settings, is_bot_admin
from src.knowledge.catalog_index import listed_image_paths, wants_send_media
from src.knowledge.catalog_rag import retrieve_catalog_context
from src.knowledge.catalog_search import CatalogSiteSearch, looks_unsure, unsure_handoff
from src.knowledge.intents import IntentMatcher, looks_identity
from src.knowledge.loader import KnowledgeLoader
from src.knowledge.product_catalogs import ai_products_snippet
from src.storage.answer_memory import AnswerMemoryStore
from src.storage.metrics import MetricsStore
from src.storage.users import UserStore
from src.ui import admin_keyboards, keyboards, messaging, texts

logger = logging.getLogger(__name__)

router = Router(name="chat")


def _is_free_text(message: Message) -> bool:
    text = (message.text or "").strip()
    if not text or text.startswith("/"):
        return False
    if text in keyboards.all_lang_button_texts():
        return False
    if text in keyboards.all_menu_button_texts():
        return False
    if text in admin_keyboards.all_admin_control_texts():
        return False
    return True


def setup_chat_router(
    settings: Settings,
    users: UserStore,
    ai: AIClient,
    intents: IntentMatcher,
    knowledge: KnowledgeLoader,
    catalog: CatalogSiteSearch,
    metrics: MetricsStore,
    access: AdminAccess | None = None,
) -> Router:
    memory = AnswerMemoryStore(settings.data_dir / "answer_memory.json")

    @router.message(F.chat.type == "private", F.text.func(lambda t: bool(t) and not str(t).startswith("/")))
    async def on_text(message: Message) -> None:
        if not _is_free_text(message):
            return
        user = message.from_user
        if not user or not message.text:
            return

        try:
            await users.touch_from_telegram_user(user)
            await _handle_ask_ai_text(message, user)
        except Exception:
            logger.exception("Ask AI handler crashed")
            try:
                lang = await users.get_lang(user.id, user.language_code)
                await message.answer(texts.t(texts.AI_ERROR, lang))
            except Exception:  # noqa: BLE001
                pass

    async def _handle_ask_ai_text(message: Message, user) -> None:
        if not await users.has_lang(user.id):
            hint = await users.get_lang(user.id, user.language_code)
            await message.answer(
                texts.t(texts.NEED_LANGUAGE_FIRST, hint),
                reply_markup=keyboards.language_keyboard(),
            )
            return

        lang = await users.get_lang(user.id, user.language_code)
        if access is not None:
            menu_kb = keyboards.main_menu_keyboard(
                lang,
                can_settings=await access.can_settings(user.id),
                can_stats=await access.can_stats(user.id),
            )
        else:
            admin = is_bot_admin(settings, user.id)
            menu_kb = keyboards.main_menu_keyboard(lang, is_admin=admin)

        if not await users.is_ask_ai(user.id):
            await message.answer(
                texts.t(texts.USE_MENU_OR_ASK_AI, lang),
                reply_markup=menu_kb,
            )
            if not await users.was_group_invited(user.id):
                await message.answer(
                    texts.t(texts.GROUP_INVITE, lang),
                    reply_markup=menu_kb,
                )
                await users.set_group_invited(user.id, True)
            return

        text = message.text.strip()
        if not text:
            return

        await metrics.record_conversation(user.id)

        if looks_identity(text):
            body = texts.bot_intro(lang)
            await users.append_chat(user.id, "user", text)
            await users.append_chat(user.id, "assistant", body)
            await metrics.record_answered(referred_support=False, ai_solved=True)
            await message.answer(
                body,
                reply_markup=keyboards.ask_ai_keyboard(
                    lang, product_id=await users.get_ask_ai_product(user.id)
                ),
            )
            return

        ask_product = await users.get_ask_ai_product(user.id)
        ask_kb = keyboards.ask_ai_keyboard(lang, product_id=ask_product)
        history = await users.get_chat_history(user.id)
        history_blob = "\n".join(
            f"{h['role']}: {h['content']}" for h in history[-8:]
        )
        retrieval = retrieve_catalog_context(
            text,
            lang=lang,
            project_root=settings.project_root,
            limit_features=4,
            limit_media=4 if wants_send_media(text) else 2,
            product_id=ask_product,
            prior_text=history_blob,
        )
        media_paths = list(retrieval.media_paths) if retrieval.attach_media else []
        if wants_send_media(text) and not media_paths and ask_product:
            media_paths = listed_image_paths(
                settings.project_root, ask_product, limit=4
            )

        if wants_send_media(text) and media_paths:
            caption = (
                "تصویر کاتالوگ همین محصول — از فایل‌های ذخیره‌شده ارسال شد."
                if (lang or "").startswith("fa")
                else "Catalog photo from stored product files."
            )
            if retrieval.units:
                body = (retrieval.units[0].body or retrieval.units[0].title or "").strip()
                if body:
                    caption = body[:1000]
            await users.append_chat(user.id, "user", text)
            await users.append_chat(user.id, "assistant", caption)
            await metrics.record_answered(referred_support=False, ai_solved=True)
            await messaging.answer_with_media(
                message, caption, images=media_paths, reply_markup=ask_kb
            )
            return

        # Local memory fast path — survives AI API changes
        mem_hit = memory.lookup(text, lang=lang)
        if (
            mem_hit is not None
            and mem_hit.score >= 12.0
            and not looks_unsure(mem_hit.answer)
            and not looks_incomplete_reply(mem_hit.answer)
            and not looks_like_reasoning_leak(mem_hit.answer)
        ):
            final = mem_hit.answer
            memory.touch_hit(mem_hit.topic_key, lang)
            await users.append_chat(user.id, "user", text)
            await users.append_chat(user.id, "assistant", final)
            await metrics.record_answered(referred_support=False, ai_solved=True)
            if media_paths:
                await messaging.answer_with_media(
                    message, final, images=media_paths, reply_markup=ask_kb
                )
            else:
                await message.answer(final, reply_markup=ask_kb)
            return

        match = intents.match(text, lang, prior_blob=history_blob)

        if (
            retrieval.insufficient
            and match.low_confidence
            and match.clarifying_question
        ):
            await users.append_chat(user.id, "user", text)
            await users.append_chat(user.id, "assistant", match.clarifying_question)
            await metrics.record_answered(referred_support=False, ai_solved=False)
            await message.answer(
                match.clarifying_question,
                reply_markup=ask_kb,
            )
            return

        wait = await message.answer(texts.t(texts.THINKING, lang))

        intent_name = match.record.intent if match.record else None
        faq_refs = match.record.faq_refs if match.record else None

        kb_limit = settings.knowledge_snippet_chars
        if retrieval.insufficient:
            kb_limit = max(kb_limit, 14000)
        kb_snip = knowledge.retrieve(
            text,
            lang,
            faq_refs=faq_refs,
            limit_chars=kb_limit,
            include_community=wants_contact_links(text) and not ask_product,
            max_chunks=8 if retrieval.insufficient else 6,
            product_id=ask_product,
        )

        # License/site catalogs are Installer-oriented — only when that product is scoped
        catalog_snip = ""
        if not ask_product or ask_product == "vpn-installer":
            catalog_snip = catalog.catalog_snippet(text, lang=lang)
        products_snip = ai_products_snippet(
            text, lang=lang, product_id=ask_product
        )
        site_snip = ""
        try:
            if (
                not ask_product
                and (
                    retrieval.insufficient
                    or match.low_confidence
                    or wants_sales_nudge(text, intent_name)
                    or wants_contact_links(text)
                )
            ):
                site_snip = await catalog.site_snippet(text)
            elif ask_product == "vpn-installer" and (
                wants_sales_nudge(text, intent_name) or wants_contact_links(text)
            ):
                site_snip = await catalog.site_snippet(text)
        except Exception:
            logger.exception("site search failed")

        intent_block = ""
        if match.record and not ask_product:
            intent_block = join_context_blocks(
                [
                    f"Matched intent: {match.record.intent} (score={match.score:.2f})",
                    f"Category: {match.record.category}",
                    f"Short answer: {match.record.short_answer}",
                    f"Full answer: {match.record.full_answer}",
                ],
                3500,
            )
        elif match.record and ask_product:
            # Soft intent hint only — do not let other-product intents override scope
            intent_block = join_context_blocks(
                [
                    f"Optional intent hint (may ignore if off-product): {match.record.intent}",
                    f"Short: {match.record.short_answer}",
                ],
                1200,
            )

        facts = format_facts_from_meta(knowledge.index.facts or intents.facts)
        system = build_system_prompt(lang, facts_block=facts)

        md_priority_note = ""
        if retrieval.insufficient and (kb_snip or "").strip():
            md_priority_note = (
                "### Fallback instruction\n"
                "Catalog feature match was weak. Prefer Product Map / FAQ markdown "
                "snippets below. Still do not invent missing facts.\n"
            )
        elif not retrieval.insufficient:
            md_priority_note = (
                "### Priority\n"
                "Prefer catalog evidence first. Use markdown/FAQ only to fill gaps.\n"
            )

        extra_sources = join_context_blocks(
            [
                retrieval.prompt_block,
                md_priority_note,
                products_snip,
                catalog_snip,
                site_snip,
            ],
            9000,
        )

        history_section = history_blob or "(none)"
        product_scope = (
            f"Product catalog scope: {ask_product}\n"
            "Answer only within this product. Do not mix other products.\n\n"
            if ask_product
            else ""
        )
        user_prompt = (
            f"{product_scope}"
            f"Prior turns in this Ask AI session:\n{history_section}\n\n"
            f"User question:\n{text}\n\n"
            f"Expanded topic hints (internal):\n{retrieval.query_expanded}\n\n"
            f"Intent context:\n{intent_block or '(none)'}\n\n"
            f"Knowledge / product-map markdown snippets:\n{kb_snip or '(none)'}\n\n"
            f"Catalog / site sources:\n{extra_sources or '(none)'}\n\n"
            "Write a helpful Telegram support reply as a real tutor/support agent.\n"
            "Source order: (1) catalog evidence, (2) product-map/FAQ markdown, "
            "(3) say insufficient if both lack the fact — never invent steps.\n"
            "When the question is educational, explain: what it is, what it is for, "
            "ordered steps, and any limit/tip present in the evidence.\n"
            "Do not list only button names. Finish every sentence completely.\n"
            "Do not invent versions or fake limits.\n"
            "If catalog lists prices and the user asked price/buy, you may quote catalog figures.\n"
            "If sources are insufficient, say you do not know and tell them to message "
            f"{SUPPORT_HANDLE}.\n"
            "Do not include website/group/@support links unless contact/purchase was asked "
            "or you are honestly handing off because you do not know.\n"
            "If the catalog media index lists a photo, it exists. Never deny that the photo exists.\n"
            "The bot sends catalog files itself. Do not say you cannot send images.\n"
            "If prior turns show Exit Server, answer Add Exit Server only — not Central Full Deploy.\n"
            "Persian: start every sentence with a Persian word; prefer Persian wording; "
            "never rename official product names "
            "(Black Fox VPN Installer & Android, Config Builder, Ask AI, 3X-UI, …).\n"
            "CRITICAL: Output ONLY the final Telegram reply. "
            "Do not write reasoning, constraint lists, or English meta analysis."
        )

        try:
            answer = await ai.chat(
                [
                    {"role": "system", "content": system},
                    {"role": "user", "content": user_prompt},
                ],
                max_tokens=max(4096, int(settings.ai_max_tokens or 4096)),
            )
        except AIClientError as exc:
            logger.exception("AI chat failed: %s", exc)
            fallback = ""
            if retrieval.units:
                fallback = "\n\n".join(
                    u.body for u in retrieval.units if (u.body or "").strip()
                ).strip()
            if not fallback and (kb_snip or "").strip():
                fallback = kb_snip.strip()[:1200]
            if not fallback and match.record:
                fallback = (
                    (match.record.full_answer or "").strip()
                    or (match.record.short_answer or "").strip()
                )
            if not fallback and (
                wants_contact_links(text) or wants_sales_nudge(text, intent_name)
            ):
                fallback = download_or_site_fallback(lang)
            if fallback:
                answer = fallback
            elif media_paths:
                answer = (
                    "تصویر کاتالوگ از فایل ذخیره‌شده ارسال می‌شود."
                    if (lang or "").startswith("fa")
                    else "Sending the stored catalog photo."
                )
            else:
                try:
                    await wait.edit_text(texts.t(texts.AI_ERROR, lang))
                except Exception:  # noqa: BLE001
                    await message.answer(texts.t(texts.AI_ERROR, lang))
                return

        answer = strip_reasoning_leak(answer)
        if looks_like_reasoning_leak(answer) or looks_incomplete_reply(answer):
            logger.warning("Ask AI reply rejected (leak/incomplete); using safe fallback")
            fallback = ""
            if retrieval.units:
                fallback = "\n\n".join(
                    u.body for u in retrieval.units if (u.body or "").strip()
                ).strip()
            if not fallback and match.record:
                fallback = (
                    (match.record.full_answer or "").strip()
                    or (match.record.short_answer or "").strip()
                )
            if wants_contact_links(text) or wants_sales_nudge(text, intent_name):
                answer = download_or_site_fallback(lang)
            elif fallback:
                answer = fallback
            elif media_paths:
                answer = (
                    "تصویر کاتالوگ از فایل ذخیره‌شده ارسال می‌شود."
                    if (lang or "").startswith("fa")
                    else "Sending the stored catalog photo."
                )
            else:
                answer = texts.t(texts.AI_ERROR, lang)

        usage = ai.last_usage
        await metrics.record_token_usage(
            prompt_tokens=usage.prompt_tokens,
            completion_tokens=usage.completion_tokens,
            total_tokens=usage.total_tokens,
            spend_usd=ai.estimate_spend_usd(usage),
        )

        final = append_sales_if_needed(
            answer,
            lang,
            user_text=text,
            intent_name=intent_name,
        )
        referred = False
        solved = True
        if looks_unsure(final):
            handoff = unsure_handoff(lang)
            if SUPPORT_HANDLE.lower() not in final.lower():
                final = f"{final.rstrip()}\n\n{handoff}"
            referred = True
            solved = False
        else:
            final = sanitize_reply_links(final, text)
            if SUPPORT_HANDLE.lower() in final.lower():
                referred = True

        if len(final) > 4000:
            final = final[:3990] + "…"

        await users.append_chat(user.id, "user", text)
        await users.append_chat(user.id, "assistant", final)
        await metrics.record_answered(referred_support=referred, ai_solved=solved)

        has_catalog = bool(retrieval.units) and not retrieval.insufficient
        has_md = bool((kb_snip or "").strip()) and (
            "product-guide:" in kb_snip or len(kb_snip) > 200
        )
        grounded = solved and not referred and (has_catalog or has_md)
        source = "catalog" if has_catalog else ("md" if has_md else "none")
        if has_catalog and has_md:
            source = "catalog+md"
        try:
            memory.remember(
                query=text,
                lang=lang,
                answer=final,
                unit_ids=[u.unit_id for u in retrieval.units],
                source=source,
                grounded=grounded,
            )
        except Exception:  # noqa: BLE001
            logger.exception("answer memory save failed")

        if media_paths:
            try:
                await wait.delete()
            except Exception:  # noqa: BLE001
                pass
            await messaging.answer_with_media(
                message,
                final,
                images=media_paths,
                reply_markup=ask_kb,
            )
        else:
            try:
                await wait.edit_text(final)
            except Exception:
                await message.answer(final, reply_markup=ask_kb)

    return router
