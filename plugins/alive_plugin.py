import os
from telegram import ParseMode
from telegram.ext import CommandHandler
from dotenv import load_dotenv
import register_plugins

def register(dispatcher, api_id, api_hash):
    dispatcher.add_handler(CommandHandler('alive', alive))

def alive(update, context):
    load_dotenv()
    owner_id = int(os.getenv('OWNER_ID'))
    sudo_users = os.getenv('SUDO_USERS').split(',')

    if update.effective_user.id == owner_id or update.effective_user.id in sudo_users:
        if len(context.args) == 0:
            # Envía el mensaje de "Estoy vivo" predeterminado si no se proporciona ningún argumento
            context.bot.send_message(chat_id=update.effective_chat.id, text="¡Estoy vivo!")
        else:
            # Obtiene los argumentos: imagen, texto y emoji
            image_url = context.args[0]
            text = " ".join(context.args[1:-1])
            emoji = context.args[-1]

            # Crea el mensaje personalizado de "Estoy vivo"
            message = f"{text} {emoji}"

            # Envía el mensaje con la imagen, el texto y el emoji
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=image_url, caption=message, parse_mode=ParseMode.MARKDOWN)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="No tienes permiso para usar este comando.")


register_plugins.register_plugin(register)