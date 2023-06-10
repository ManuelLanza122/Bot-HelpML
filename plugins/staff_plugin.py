import os
import json
from telegram import ParseMode
from telegram.ext import CommandHandler
from register_plugin import register_plugin

STAFF_FILE = 'staff.json'

def register(bot, api_id, api_hash):
    bot.add_handler(CommandHandler('staff', show_staff))
    bot.add_handler(CommandHandler('addstaff', add_staff))

def show_staff(update, context):
    chat_id = update.effective_chat.id

    if os.path.exists(STAFF_FILE):
        with open(STAFF_FILE, 'r') as file:
            staff_data = json.load(file)

        if str(chat_id) in staff_data:
            staff_text = staff_data[str(chat_id)]
            context.bot.send_message(chat_id=chat_id, text=staff_text, parse_mode=ParseMode.MARKDOWN)
        else:
            context.bot.send_message(chat_id=chat_id, text="No se ha definido información del staff para este grupo.")
    else:
        context.bot.send_message(chat_id=chat_id, text="No se ha definido información del staff para este grupo.")

def add_staff(update, context):
    chat_id = update.effective_chat.id
    staff_text = ' '.join(context.args)

    if staff_text:
        if os.path.exists(STAFF_FILE):
            with open(STAFF_FILE, 'r') as file:
                staff_data = json.load(file)
        else:
            staff_data = {}

        staff_data[str(chat_id)] = staff_text

        with open(STAFF_FILE, 'w') as file:
            json.dump(staff_data, file)

        context.bot.send_message(chat_id=chat_id, text="Se ha actualizado la información del staff del grupo.")
    else:
        context.bot.send_message(chat_id=chat_id, text="Por favor, proporciona la información del staff del grupo.")

register_plugin(dispatcher, api_id, api_hash)