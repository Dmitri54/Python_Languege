from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import *


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}!')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'/hi\n/time\n/help') # Возвращает информацию о комманде (/hi\)
# о комманде (/time\) и самой себе (/help)


async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

# Функция сложения:
async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE): # Информация от пользователя приходит в виде текста.
    log(update, context)
    msg = update.message.text # Сообщение пользователя, которое я положу в отдельную переменную.
    print(msg) # Покажет, что переменная точно сохранена.
    items = msg.split() # /sum 123 534543
    x = int(items[1])
    y = int(items[2])

    await update.message.reply_text(f'{x} + {y} = {x + y}')