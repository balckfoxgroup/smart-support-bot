# Catalog inbox / wizard

## From Telegram Settings

1. Open **📦 ساخت کاتالوگ از پوشه**
2. Optionally toggle sources: site / channel / group (from Main Info)
3. Either:
   - send a **folder path on the bot server** (any OS path the bot process can read), or
   - **upload** ZIP / text / photos in the chat
4. Tap **✅ ساخت کاتالوگ**

The bot:
- copies materials into `catalog_inbox/<product>/`
- copies photos into `media/catalogs/<product>/`
- builds `product_catalogs/<product>.json` with AI
- keeps a copy `*.catalog.json` inside the inbox folder

## Manual server folders

You can still place files under `catalog_inbox/my-product/` and use the wizard path.
