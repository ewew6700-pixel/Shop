import os
from flask import Flask
from threading import Thread
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# --- CONFIGURATION SÉCURISÉE ---
# On demande à Render de nous donner le secret
TOKEN = os.environ.get("BOT_TOKEN")
URL_SITE = "https://ewew6700-pixel.github.io/Shop/"

app = Flask(__name__)
@app.route('/')
def home(): return "OK"

def run():
    app.run(host='0.0.0.0', port=10000)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kb = [[InlineKeyboardButton("🛍️ OUVRIR LE SHOP", web_app=WebAppInfo(url=URL_SITE))]]
    await update.message.reply_text("🔥 BIENVENUE !", reply_markup=InlineKeyboardMarkup(kb))

if __name__ == '__main__':
    Thread(target=run).start()
    if TOKEN:
        print("Démarrage...")
        ApplicationBuilder().token(TOKEN).build().add_handler(CommandHandler("start", start)).run_polling()
