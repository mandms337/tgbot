import os
import openai
import telebot
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))
openai.api_key = os.getenv('OPENAI_KEY')

@bot.message_handler(commands=['start'])
def cmd_start(message):
    try :
        response = openai.ChatCompletion.create(
            model = 'gpt-4' ,
            messages = [{'role': 'user', 'content': message.text}]
        )
        bot.reply_to(message , response['choises'][0]['message']['content'])
    except Exception as e :
        bot.reply_to(message , 'Ошибка:' + str(e))


@bot.message_handler(commands=['help'])
def any_text(message):
    bot.send_message(message.chat.id, 'Я пока ничего не могу')


if __name__ == '__main__':
    bot.polling(none_stop=True)
