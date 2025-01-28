import telebot

bot = telebot.TeleBot('7581915376:AAG8FWud6rpdfM7tRhVgaWmz19-AeX9Gogg')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,'Привет , опять тупишь , чем помочь , гений?')

bot.polling(none_stop=True)



