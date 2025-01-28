import logging

import telebot
from telebot.types import Message


bot = telebot.TeleBot('7581915376:AAG8FWud6rpdfM7tRhVgaWmz19-AeX9Gogg')

@bot.message_handler(commands=['start'])
def cmd_start(message: Message):
    bot.send_message(message.chat.id,'Привет , опять тупишь , чем помочь , гений?')


@bot.message_handler(content_types=['text'])
def any_text(message: Message):
    bot.send_message(message.chat.id, str(reversed(message.text)))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    bot.polling(none_stop=True, logger_level=logging.INFO)
