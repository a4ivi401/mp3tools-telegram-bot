import telebot
from config import API_TOKEN
from handlers import start_handler, audio_handler, help_handler, info_handler, convert_handler

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def cmd_start(message):
  start_handler(message, bot)

@bot.message_handler(content_types=['audio'])
def handle_audio(message):
  audio_handler(message, bot)

@bot.message_handler(commands=['help'])
def cmd_help(message):
  help_handler(message, bot)

@bot.message_handler(func=lambda message: message.text == "Информация о боте")
def process_info(message):
  info_handler(message, bot)

@bot.message_handler(func=lambda message: message.text == "Конвертация аудио")
def process_convert(message):
  convert_handler(message, bot)

if __name__ == '__main__':
  bot.polling(non_stop=True)