import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, Message

TOKEN = "7975587876:AAEPJnx7pt-qeqM41ijxg6dRU_wfzgEx1aA"
bot = telebot.TeleBot(TOKEN)

def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(KeyboardButton("📺 قناتي على اليوتيوب"), KeyboardButton("📷 حسابي على انستقرام"))
    markup.row(KeyboardButton("📘 حسابي على فيسبوك"), KeyboardButton("💬 جروب الدردشة"))
    markup.row(KeyboardButton("🎮 سيرفري على ديسكورد"), KeyboardButton("💬 تواصل معي"))
    return markup

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "أهلين بالأسطورة منور ✨🔥👋", reply_markup=main_menu())

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, "📌 أوامر البوت:\n"
                                      "🔹 /start - لعرض القائمة الرئيسية\n"
                                      "🔹 /help - لعرض هذه الرسالة\n"
                                      "🔹 يمكنك استخدام الأزرار للحصول على الروابط بسهولة")

@bot.message_handler(func=lambda message: message.text == "📺 قناتي على اليوتيوب")
def youtube(message):
    bot.send_message(message.chat.id, "📺 قناتي على اليوتيوب:\nhttps://youtube.com/@popxevgames-v1w")

@bot.message_handler(func=lambda message: message.text == "📷 حسابي على انستقرام")
def instagram(message):
    bot.send_message(message.chat.id, "📷 حسابي على انستقرام:\nhttps://www.instagram.com/popxev_games")

@bot.message_handler(func=lambda message: message.text == "📘 حسابي على فيسبوك")
def facebook(message):
    bot.send_message(message.chat.id, "📘 حسابي على فيسبوك:\nhttps://www.facebook.com/share/1Dsxdcv7yN/")

@bot.message_handler(func=lambda message: message.text == "💬 جروب الدردشة")
def telegram_group(message):
    bot.send_message(message.chat.id, "💬 جروب الدردشة على تيليجرام:\nhttps://t.me/Popxevgamesgroup")

@bot.message_handler(func=lambda message: message.text == "🎮 سيرفري على ديسكورد")
def discord(message):
    bot.send_message(message.chat.id, "🎮 سيرفري على ديسكورد:\nhttps://discord.gg/tuRy8Qf7")

@bot.message_handler(func=lambda message: message.text == "💬 تواصل معي")
def contact_me(message):
    mention_text = f'<a href="tg://user?id=6087883512">اضغط هنا</a>'
    bot.send_message(message.chat.id, f"💬 يمكنك التواصل معي هنا: {mention_text}", parse_mode="HTML")

BANNED_WORDS = ["كس", "أمك", "امك", "شرموطة", "نقش", "قحبة", "شرموط", "قحبه", "كلب", "حمار", "fack", "fy", "nik"]

@bot.message_handler(func=lambda message: any(word in message.text.lower() for word in BANNED_WORDS))
def delete_bad_words(message: Message):
    try:
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, "🚫 تم حذف رسالة تحتوي على كلمات غير مسموح بها!")
    except Exception as e:
        print(f"خطأ أثناء حذف الرسالة: {e}")

bot.polling()
