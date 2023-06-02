
from telegram.ext import *
from telegram import KeyboardButton, ReplyKeyboardMarkup
from settings import TOKEN
from telegram.constants import ParseMode
from mongodb import get_vacancies
import pytz


async def start_commmand(update, _):
    current_id = update.message.chat['id']
    admin_id = 5500834174
    keyboard = []
    if current_id != admin_id:
        keyboard = [[ KeyboardButton('Добавить вакансию')]]
    else:
        keyboard = [[KeyboardButton("Получить список вакансий")]]  
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text('Добро пожаловать!', reply_markup=reply_markup)

async def show_vacancies(update, _):
    answer = update.message.text
    if answer == 'Получить список вакансий':
        current_vacancies =  get_vacancies()
        text = ''
        for vac in current_vacancies:
            text += str(vac['title']) + '\n'
            text += str(vac['salary']) + '\n'
            text += str(vac['description']) + '\n'
            text += '\n'
        

        await update.message.reply_text(text)

if __name__ == '__main__':
    application = Application.builder().token(TOKEN).build()

    # Commands
    application.add_handler(CommandHandler('start', start_commmand))
    application.add_handler(MessageHandler(filters.TEXT, show_vacancies))

    # Run bot
    application.run_polling(1.0)



    # id администратора = 5500834174