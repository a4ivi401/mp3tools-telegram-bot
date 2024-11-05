import os
from telebot import types
from audio_converter import converter_audio
from config import SUPPORTED_FORMATS

def start_handler(message, bot):
  bot.send_message(message.chat.id, "Привет! Я бот для работы с аудиофайлами. Используйте команды для конвертации.")

def audio_handler(message, bot):
    audio_file = bot.get_file(message.audio.file_id)
    downloaded_file = bot.download_file(audio_file.file_path)
    
    input_file = 'input.ogg'
    with open(input_file, 'wb') as new_file:
        new_file.write(downloaded_file)

    # Предложение формата для конвертации
    format_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    selected_format = message.audio.mime_type.split('/')[1]  # Получаем текущий формат
    available_formats = [fmt for fmt in SUPPORTED_FORMATS if fmt != selected_format]

    for fmt in available_formats:
        format_keyboard.add(types.KeyboardButton(fmt))
    
    bot.send_message(message.chat.id, "Выберите формат для конвертации:", reply_markup=format_keyboard)

    # Сохраняем информацию о файле и чате для дальнейшей обработки
    bot.register_next_step_handler(message, lambda m: process_conversion(m, input_file, bot))


def process_conversion(message, input_file, bot):
  selected_format = message.text.lower()

  if selected_format in SUPPORTED_FORMATS:
     output_file = converter_audio(input_file, selected_format)
     with open(output_file, 'rb') as audio:
        bot.send_audio(message.chat.id, audio)

        os.remove(input_file)
        os.remove(output_file)
  else:
     bot.send_message(message.chat.id, "Неверный формат. Пожалуйста, попробуйте снова.")

def help_handler(message, bot):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_info = types.KeyboardButton("Информация о боте")
    button_convert = types.KeyboardButton("Конвертация аудио")
    keyboard.add(button_info, button_convert)
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=keyboard)

def info_handler(message, bot):
    bot.send_message(message.chat.id, "Я бот для конвертации аудиофайлов!")

def convert_handler(message, bot):
    bot.send_message(message.chat.id, "Отправьте мне аудиофайл для конвертации.")
