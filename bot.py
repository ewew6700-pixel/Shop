import os
from flask import Flask
from threading import Thread
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 1. On récupère les infos
TOKEN = os.environ.get("BOT_TOKEN")
URL_SITE = "https://ewew6700-pixel.github.io/Shop/"

# 2. Serveur Flask léger pour Render
app = Flask(__name__)
@app.route('/')
def index():
    return "Statut : OK"

def run():
    app.run(host='0.0.0.0', port=10000) # Port standard Render

# 3. La commande Start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kb = [[InlineKeyboardButton("🛍️ OUVRIR LE SHOP", web_app=WebAppInfo(url=URL_SITE))]]
    await update.message.reply_text("Bienvenue !", reply_markup=InlineKeyboardMarkup(kb))

if __name__ == '__main__':
    # Lance le serveur dans un coin
    Thread(target=run).start()
    
    # Lance le bot
    if TOKEN:
        print("Démarrage du bot...")
        bot = ApplicationBuilder().token(TOKEN).build()
        bot.add_handler(CommandHandler("start", start))
        bot.run_polling()
