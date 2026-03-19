from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8769832794:AAHJFUXinfpSxFt5Ya0H5O3FchqvNf_RkOo"
URL_SITE = "https://ewew6700-pixel.github.io/Shop/"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bouton = InlineKeyboardButton("🛒 OUVRIR LE SHOP", web_app=WebAppInfo(url=URL_SITE))
    clavier = InlineKeyboardMarkup([[bouton]])
    await update.message.reply_text("Bienvenue chez BIGO 67 ! 🌴", reply_markup=clavier)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
print("✅ BOT LANCE AVEC SUCCES !")
app.run_polling()
