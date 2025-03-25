import telebot
import ReplyKeyboardMarkup, Keyboar>


TOKEN = "7975587876:AAEPJnx7pt-qeqM41ijxg6dRU_wfzgEx1a>
bot = telebot.TeleBot(TOKEN)

markup = ReplyKeyboardMarkup(resize_keyboard=True)
markup.row(KeyboardButton("💬 تواصل معي"), KeyboardBut>
markup.row(KeyboardButton("📸 حسابي على إنستجرام"), Ke>
markup.row(KeyboardButton("🎮 جروب ديسكورد"), Keyboard>

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(
        message.chat.id,
        "أهلين بالأسطورة منور ✨🔥👋\nاختر أحد الأزرار>
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: message.text>
def contact_me(message):
    mention_text = f'<a href="tg://user?id=6087883512">
    bot.reply_to(message, f"يمكنك التواصل معي هنا: {me>

@bot.message_handler(func=lambda message: message.text>
def youtube(message):
    bot.reply_to(message, "📺 قناتي على يوتيوب:\nhttps>

@bot.message_handler(func=lambda message: message.text>
def instagram(message):
    bot.reply_to(message, "📸 حسابي على إنستجرام:\nhtt>

@bot.message_handler(func=lambda message: message.text>
def facebook(message):
    bot.reply_to(message, "📘 صفحتي على فيسبوك:\nhttps>

@bot.message_handler(func=lambda message: message.text>
def discord(message):
    bot.reply_to(message, "🎮 جروب ديسكورد:\nhttps://d>

@bot.message_handler(func=lambda message: message.text>
def telegram_group(message):
    bot.reply_to(message, "💬 جروب تيليجرام:\nhttps://>

bot.polling()
