import telebot
import os
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = os.getenv("BOT_TOKEN")  
bot = telebot.TeleBot(TOKEN)

markup = ReplyKeyboardMarkup(resize_keyboard=True)
markup.row(KeyboardButton("💬 تواصل معي"), KeyboardButton("📺 قناتي على يوتيوب"))
markup.row(KeyboardButton("📸 حسابي على إنستجرام"), KeyboardButton("📘 صفحتي على فيسبوك"))
markup.row(KeyboardButton("🎮 جروب ديسكورد"), KeyboardButton("💬 جروب تيليجرام"))

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(
        message.chat.id,
        "أهلين بالأسطورة منور ✨🔥👋\nاختر أحد الأزرار:",
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: message.text == "💬 تواصل معي")
def contact_me(message):
    mention_text = f'<a href="tg://user?id=6087883512">اضغط هنا</a>'
    bot.reply_to(message, f"يمكنك التواصل معي هنا: {mention_text}", parse_mode="HTML")

@bot.message_handler(func=lambda message: message.text == "📺 قناتي على يوتيوب")
def youtube(message):
    bot.reply_to(message, "📺 قناتي على يوتيوب:\nhttps://youtube.com/@popxevgames-v1w?si=QulhnL1ZbhMU3mDK")

@bot.message_handler(func=lambda message: message.text == "📸 حسابي على إنستجرام")
def instagram(message):
    bot.reply_to(message, "📸 حسابي على إنستجرام:\nhttps://www.instagram.com/popxev_games?igsh=anNwdzR5dXFwc2E4")

@bot.message_handler(func=lambda message: message.text == "📘 صفحتي على فيسبوك")
def facebook(message):
    bot.reply_to(message, "📘 صفحتي على فيسبوك:\nhttps://www.facebook.com/share/1Dsxdcv7yN/")

@bot.message_handler(func=lambda message: message.text == "🎮 جروب ديسكورد")
def discord(message):
    bot.reply_to(message, "🎮 جروب ديسكورد:\nhttps://discord.gg/tuRy8Qf7")

@bot.message_handler(func=lambda message: message.text == "💬 جروب تيليجرام")
def telegram_group(message):
    bot.reply_to(message, "💬 جروب تيليجرام:\nhttps://t.me/Popxevgamesgroup")

bot.polling()
