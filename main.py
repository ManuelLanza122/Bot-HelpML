import os
import importlib
from dotenv import load_dotenv
from telegram.ext import Updater

# Directorio donde se encuentran los plugins
PLUGINS_DIR = 'plugins'

def load_plugins():
    plugins = []
    plugin_files = os.listdir(PLUGINS_DIR)

    for plugin_file in plugin_files:
        if plugin_file.endswith('.py'):
            plugin_name = plugin_file[:-3]
            module_name = f"{PLUGINS_DIR}.{plugin_name}"
            plugin = importlib.import_module(module_name)
            plugins.append(plugin)

    return plugins

def register_plugins(dispatcher, api_id, api_hash):
    plugins = load_plugins()

    for plugin in plugins:
        if hasattr(plugin, 'register'):
            plugin.register(dispatcher, api_id, api_hash)

def main():
    # Carga las variables de entorno desde el archivo .env
    load_dotenv()

    # Obtiene los valores de las variables de entorno
    api_id = os.getenv('API_ID')
    api_hash = os.getenv('API_HASH')
    token = os.getenv('TOKEN')
    owner_id = int(os.getenv('OWNER_ID'))

    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher

    # Registra los plugins y pasa los valores de API ID y API Hash
    register_plugins(dispatcher, api_id, api_hash)

    # Añade el propietario como "sudo" autorizado
    add_sudo_user(owner_id, dispatcher.bot_data)

    # Inicia el bot
    updater.start_polling()
    updater.idle
