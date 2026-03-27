import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8745981995:AAHhj4pLsyc_NKCCGCVovgGYRsjmtRpbL6g"

# 🔹 FAQ DATA
faq_data = {
    "hi": "Hello! Welcome to Golden Blush 💄",
    "price": "Our services start from 50 AED.",
    "facial": "We offer Glow, Gold & Glass Skin facials ✨",
    "offer": "🔥 Facial + Pedicure + Threading = 150 AED",
    "location": "📍 We are in Sharjah",
    "timing": "🕒 10 AM to 9 PM",
    "hair": "We do Haircuts, Styling, Smoothing & Coloring",
    "book": "📞 Call +971 XXXXXXXX to book"
}

# 🔹 QUOTES
quotes = [
    "Believe in yourself and all that you are.",
    "Push yourself, because no one else will do it for you.",
    "Success is not final, failure is not fatal.",
    "Dream big. Start small. Act now.",
    "Great things never come from comfort zones."
]

# 🔹 RESPONSE ENGINE
def get_response(user_input):
    user_input = user_input.lower()

    # Motivational
    if "motivate" in user_input or "quote" in user_input:
        return "✨ " + random.choice(quotes)

    # FAQ matching
    for keyword in faq_data:
        if keyword in user_input:
            return faq_data[keyword]

    return "Sorry, I didn’t understand. Ask about services, price, or type 'motivate me' 😊"


# 🔹 TELEGRAM HANDLERS
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hi! I'm your Golden Blush Assistant 💄\n"
        "You can ask about services, prices, or type 'motivate me' ✨"
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    response = get_response(user_text)
    await update.message.reply_text(response)


# 🔹 RUN BOT
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("🚀 Bot running...")
app.run_polling()