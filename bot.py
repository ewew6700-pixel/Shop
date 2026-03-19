import os
from flask import Flask
from threading import Thread
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# --- CONFIGURATION ---
# On utilise BOT_TOKEN pour que GitHub ne bloque pas ton compte
TOKEN = os.environ.get("BOT_TOKEN")
URL_SITE = "https://ewew6700-pixel.github.io/Shop/"

# --- SYSTÈME ANTI-COUPURE RENDER ---
app = Flask('')

@app.route('/')
def home():
    return "Bot Bigo 67 en ligne !"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# --- LOGIQUE DU BOT ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bouton = InlineKeyboardButton("🛍️ OUVRIR LE SHOP", web_app=WebAppInfo(url=URL_SITE))
    clavier = InlineKeyboardMarkup([[bouton]])
    await update.message.reply_text("Bienvenue chez BIGO 67 ! 🌴", reply_markup=clavier)

if __name__ == '__main__':
    # On vérifie que le token est présent
    if TOKEN:
        # Lancement du serveur Web en arrière-plan
        keep_alive()
        
        # Lancement du Bot Telegram
        bot_app = ApplicationBuilder().token(TOKEN).build()
        bot_app.add_handler(CommandHandler("start", start))
        
        print("✅ BOT LANCE AVEC SUCCES !")
        bot_app.run_polling()
    else:
        print("❌ ERREUR : Aucun Token trouvé sur Render !")
