import os
import json
from dotenv import load_dotenv
from telegram.ext import CommandHandler, Filters
import register_plugins

GBAN_FILE = 'gban.json'

def register(dispatcher, api_id, api_hash):
    dispatcher.add_handler(CommandHandler('gban', gban))

def gban(update, context):
    user_id = update.effective_user.id
    username = update.effective_user.username

    if is_sudo_or_owner(user_id):
        if len(context.args) == 1:
            target_user = context.args[0]
            if target_user.startswith('@'):
                target_user = target_user[1:]  # Remove '@' symbol
            add_to_gban_list(target_user)
            context.bot.send_message(chat_id=update.effective_chat.id, text=f"Usuario {target_user} baneado a nivel global.")
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Debes proporcionar el nombre de usuario del usuario que deseas banear.")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="No tienes permisos para realizar un ban global.")

def is_sudo_or_owner(user_id):
    owner_id = int(os.getenv('OWNER_ID'))
    sudo_users = os.getenv('SUDO_USERS').split(',')

    return user_id == owner_id or str(user_id) in sudo_users

def add_to_gban_list(username):
    if not os.path.exists(GBAN_FILE):
        gban_list = []
    else:
        with open(GBAN_FILE, 'r') as file:
            gban_list = json.load(file)

    if username not in gban_list:
        gban_list.append(username)

    with open(GBAN_FILE, 'w') as file:
        json.dump(gban_list, file)

load_dotenv()
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

# Crea el Updater y el Dispatcher

register_plugins.register_plugin(register)