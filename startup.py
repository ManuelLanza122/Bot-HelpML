from dotenv import load_dotenv
from telegram.ext import Updater
from config import TOKEN, OWNER_ID
from plugins import register_plugins

def load_environment():
    load_dotenv()  # Carga las variables de entorno desde el archivo .env

def setup_bot():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Registra los plugins y pasa los valores necesarios
    register_plugins(dispatcher, OWNER_ID)

    return updater

def start_bot(updater):
    updater.start_polling()
    updater.idle()

def run_startup():
    load_environment()
    updater = setup_bot()
    start_bot(updater)

if name == 'main':
    run_startup()