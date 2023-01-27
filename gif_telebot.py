import telebot
import random
from telebot import types
import os

# Создаем бота
bot = telebot.TeleBot('Токен')
# Команда start
@bot.message_handler(commands=["start"])
def start(m, res=False):
        # Добавляем две кнопки
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Animals")
        item2=types.KeyboardButton("Secrets")
        markup.add(item1)
        markup.add(item2)
        bot.send_message(m.chat.id, 'Выбери какую Гифку прислать',  reply_markup=markup)
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # гифка
    if message.text.strip() == 'Animals' :
        photo = open('animals/' + random.choice(os.listdir('animals')), 'rb')
        bot.send_animation(message.from_user.id, photo)
    # еще гифка
    elif message.text.strip() == 'Secrets':
        photo = open('Secrets/' + random.choice(os.listdir('Secrets')), 'rb')
        bot.send_animation(message.from_user.id, photo)

# Запускаем бота
bot.polling(none_stop=True, interval=0)