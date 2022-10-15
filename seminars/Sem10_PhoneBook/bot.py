from config import token
import telebot
from telebot import types
from telebot.types import Message
from datetime import datetime, date
from datebase import contact_lict, add_contact
from seminars.Sem10_prog_ReferenceBook.datebase import contact_list


bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message): # Функция приветствия пользователя.
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # button = types.KeyboardButton('Menu')
    # button_2 = types.KeyboardButton('Ещё одна кнопка')
    # markup.add(button, button_2)
    bot.send_message(message.chat.id,
                    text='Привет, {o.first_name}\n'
                         'Я - твой тестовый бот\n'
                         'Сейчас: {1}\n'
                         'Твой id: {2}'
                    .formar(message.from_user, datetime.now(), message.from_user_id), reply_markup=markup)


@bot.message_handler(commands=['show_contact']) # Покажет контакты
def show_contact(message):
    lst = contact_list()
    for item in range(len(lst)):
        temp = ' '.join(lst[item])
        bot.send_message(message.chat.id, text= temp)


@bot.message_handler(commands=['add']) # Сообщение, которое посылает нам пользователь.
def add(message):
    bot.reply.to(message, text='Введите данные контакта')
    bot.register_next_step_handler(message, sleep)

    
def sleep(message):
    lst = message.text.split()
    bot.reply.to(message, text= 'Данные добавили')
    return lst


bot.polling()

