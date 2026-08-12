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
    looks_like_reasoning_leak,
    sanitize_reply_links,
    strip_reasoning_leak,
    wants_contact_links,
    wants_sales_nudge,
)
from src.config import Settings, is_bot_admin
from src.knowledge.catalog_search import CatalogSiteSearch, looks_unsure, unsure_handoff
from src.knowledge.intents import IntentMatcher, looks_identity
from src.knowledge.loader import KnowledgeLoader
from src.knowledge.product_catalogs import ai_products_snippet
from src.storage.metrics import MetricsStore
from src.storage.users import UserStore
from src.ui import admin_keyboards, keyboards, texts

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
) -> Router:
    @router.message(F.chat.type == "private", F.text.func(lambda t: bool(t) and not str(t).startswith("/")))
    async def on_text(message: Message) -> None:
        if not _is_free_text(message):
            return
        user = message.from_user
        if not user or not message.text:
            return

        if not await users.has_lang(user.id):
            hint = await users.get_lang(user.id, user.language_code)
            await message.answer(
                texts.t(texts.NEED_LANGUAGE_FIRST, hint),
                reply_markup=keyboards.language_keyboard(),
            )
            return

        lang = await users.get_lang(user.id, user.language_code)
        admin = is_bot_admin(settings, user.id)

        if not await users.is_ask_ai(user.id):
            await message.answer(
                texts.t(texts.USE_MENU_OR_ASK_AI, lang),
                reply_markup=keyboards.main_menu_keyboard(lang, is_admin=admin),
            )
            if not await users.was_group_invited(user.id):
                await message.answer(
                    texts.t(texts.GROUP_INVITE, lang),
                    reply_markup=keyboards.main_menu_keyboard(lang, is_admin=admin),
                )
                await users.set_group_invited(user.id, True)
            return

        text = message.text.strip()
        if not text:
            return

        await metrics.record_conversation(user.id)

        # Fast path: introduce yourself
        if looks_identity(text):
            body = texts.bot_intro(lang)
            await users.append_chat(user.id, "user", text)
            await users.append_chat(user.id, "assistant", body)
            await metrics.record_answered(referred_support=False, ai_solved=True)
            await message.answer(body, reply_markup=keyboards.ask_ai_keyboard(lang))
            return

        history = await users.get_chat_history(user.id)
        history_blob = "\n".join(
            f"{h['role']}: {h['content']}" for h in history[-6:]
        )

        match = intents.match(text, lang, prior_blob=history_blob)

        if match.low_confidence and match.clarifying_question:
            await users.append_chat(user.id, "user", text)
            await users.append_chat(user.id, "assistant", match.clarifying_question)
            await metrics.record_answered(referred_support=False, ai_solved=False)
            await message.answer(
                match.clarifying_question,
                reply_markup=keyboards.ask_ai_keyboard(lang),
            )
            return

        wait = await message.answer(texts.t(texts.THINKING, lang))

        intent_name = match.record.intent if match.record else None
        faq_refs = match.record.faq_refs if match.record else None

        kb_snip = knowledge.retrieve(
            text,
            lang,
            faq_refs=faq_refs,
            limit_chars=settings.knowledge_snippet_chars,
            include_community=wants_contact_links(text),
        )

        catalog_snip = catalog.catalog_snippet(text, lang=lang)
        products_snip = ai_products_snippet(text, lang=lang)
        site_snip = ""
        try:
            # Fetch site when catalog alone is thin or question is open-ended
            if match.low_confidence or wants_sales_nudge(text, intent_name) or wants_contact_links(text):
                site_snip = await catalog.site_snippet(text)
        except Exception:
            logger.exception("site search failed")

        intent_block = ""
        if match.record:
            intent_block = join_context_blocks(
                [
                    f"Matched intent: {match.record.intent} (score={match.score:.2f})",
                    f"Category: {match.record.category}",
                    f"Short answer: {match.record.short_answer}",
                    f"Full answer: {match.record.full_answer}",
                ],
                4000,
            )

        facts = format_facts_from_meta(knowledge.index.facts or intents.facts)
        system = build_system_prompt(lang, facts_block=facts)

        extra_sources = join_context_blocks(
            [products_snip, catalog_snip, site_snip],
            7000,
        )

        history_section = history_blob or "(none)"
        user_prompt = (
            f"Prior turns in this Ask AI session:\n{history_section}\n\n"
            f"User question:\n{text}\n\n"
            f"Intent context:\n{intent_block or '(none)'}\n\n"
            f"Knowledge snippets:\n{kb_snip or '(none)'}\n\n"
            f"Catalog / site sources:\n{extra_sources or '(none)'}\n\n"
            "Write a helpful Telegram support reply.\n"
            "Do not invent versions or fake limits.\n"
            "If catalog lists prices and the user asked price/buy, you may quote catalog figures.\n"
            "If sources are insufficient, say you do not know and tell them to message "
            f"{SUPPORT_HANDLE}.\n"
            "Do not include website/group/@support links unless contact/purchase was asked "
            "or you are honestly handing off because you do not know.\n"
            "If prior turns show Exit Server, answer Add Exit Server only — not Central Full Deploy.\n"
            "Persian: start every sentence with a Persian word; prefer Persian wording; "
            "never rename official product names (Config Builder, Installer, Ask AI, 3X-UI, …).\n"
            "CRITICAL: Output ONLY the final Telegram reply. "
            "Do not write reasoning, constraint lists, or English meta analysis."
        )

        try:
            answer = await ai.chat(
                [
                    {"role": "system", "content": system},
                    {"role": "user", "content": user_prompt},
                ]
            )
        except AIClientError as exc:
            logger.exception("AI chat failed: %s", exc)
            if wants_contact_links(text) or wants_sales_nudge(text, intent_name):
                answer = download_or_site_fallback(lang)
            else:
                await wait.edit_text(texts.t(texts.AI_ERROR, lang))
                return

        answer = strip_reasoning_leak(answer)
        if looks_like_reasoning_leak(answer):
            logger.warning("Ask AI reasoning leak blocked; using safe fallback")
            if wants_contact_links(text) or wants_sales_nudge(text, intent_name):
                answer = download_or_site_fallback(lang)
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
        # Keep support handle when honestly unsure
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

        try:
            await wait.edit_text(final)
        except Exception:
            await message.answer(final)

    return router
