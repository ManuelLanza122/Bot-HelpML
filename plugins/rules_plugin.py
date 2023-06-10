import os
import json
from telegram import ParseMode
from telegram.ext import CommandHandler
from register_plugin import register_plugin

RULES_FILE = 'rules.json'

def register(bot, api_id, api_hash):
    bot.add_handler(CommandHandler('rules', rules))
    bot.add_handler(CommandHandler('setrules', set_rules))

def rules(update, context):
    chat_id = update.effective_chat.id

    if os.path.exists(RULES_FILE):
        with open(RULES_FILE, 'r') as file:
            rules_data = json.load(file)

        if str(chat_id) in rules_data:
            rules_text = rules_data[str(chat_id)]
            context.bot.send_message(chat_id=chat_id, text=rules_text, parse_mode=ParseMode.MARKDOWN)
        else:
            context.bot.send_message(chat_id=chat_id, text="No se han definido reglas para este grupo.")
    else:
        context.bot.send_message(chat_id=chat_id, text="No se han definido reglas para este grupo.")

def set_rules(update, context):
    chat_id = update.effective_chat.id
    rules_text = ' '.join(context.args)

    if rules_text:
        if os.path.exists(RULES_FILE):
            with open(RULES_FILE, 'r') as file:
                rules_data = json.load(file)
        else:
            rules_data = {}

        rules_data[str(chat_id)] = rules_text

        with open(RULES_FILE, 'w') as file:
            json.dump(rules_data, file)

        context.bot.send_message(chat_id=chat_id, text="Se han actualizado las reglas del grupo.")
    else:
        context.bot.send_message(chat_id=chat_id, text="Por favor, proporciona las nuevas reglas del grupo.")

register_plugin(dispatcher, api_id, api_hash)