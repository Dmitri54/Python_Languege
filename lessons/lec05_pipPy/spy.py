# Метод логирования сообщений, которые присылаются Боту.

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

path = r'/Users/User/Desktop/Python_Language/lessons/lec05_pipPy/db.csv'

async def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = open('path', 'a')
    file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}\n')
    file.close() # Закроет фаил.
