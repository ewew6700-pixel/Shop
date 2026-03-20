import os
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler

TOKEN = os.environ.get("BOT_TOKEN")
URL_SITE = "https://ewew6700-pixel.github.io/Shop/"

async def start(update: Update, context):
    kb = [[InlineKeyboardButton("🛍️ OUVRIR LE SHOP", web_app=WebAppInfo(url=URL_SITE))]]
    await update.message.reply_text("🔥 BIENVENUE !", reply_markup=InlineKeyboardMarkup(kb))

def main():
    if not TOKEN:
        print("Erreur: Pas de Token !")
        return
    
    # On construit l'application simplement
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    print("✅ BOT PRET !")
    app.run_polling(drop_pending_updates=True)

if __name__ == '__main__':
    main()
