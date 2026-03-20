import os
from flask import Flask
from threading import Thread
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# --- CONFIGURATION ---
# On récupère le Token que tu as mis dans l'onglet Environment de Render
TOKEN = os.environ.get("BOT_TOKEN")
URL_SITE = "https://ewew6700-pixel.github.io/Shop/"

# --- MINI SERVEUR POUR RENDER ---
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    # Render utilise le port 10000 par défaut
    app.run(host='0.0.0.0', port=10000)

def keep_alive():
    t = Thread(target=run)
    t.start()

# --- COMMANDE DU BOT ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bouton = InlineKeyboardButton("🛍️ OUVRIR LE SHOP", web_app=WebAppInfo(url=URL_SITE))
    clavier = InlineKeyboardMarkup([[bouton]])
    await update.message.reply_text("Bienvenue chez BIGO 67 ! 🌴", reply_markup=clavier)

if __name__ == '__main__':
    if TOKEN:
        # 1. On lance le serveur web en arrière-plan
        keep_alive()
        
        # 2. On lance le bot Telegram
        bot_app = ApplicationBuilder().token(TOKEN).build()
        bot_app.add_handler(CommandHandler("start", start))
        
        print("✅ BOT LANCE AVEC SUCCES !")
        bot_app.run_polling()
    else:
        print("❌ ERREUR : Aucun TOKEN trouvé !")
