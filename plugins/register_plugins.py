from telegram.ext import Dispatcher
from plugins import (
    afk_plugin,
    alive_plugin,
    gban_plugin,
    group_commands_plugin,
    rules_plugin,
    staff_plugin,
    sudo_plugin,
    userinfo_plugin,
    welcome_plugin
)

def register_plugins(dispatcher, api_id, api_hash):
    # Registra los plugins
    afk_plugin.register(dispatcher)
    alive_plugin.register(dispatcher)
    gban_plugin.register(dispatcher)
    group_commands_plugin.register(dispatcher, api_id, api_hash)
    rules_plugin.register(dispatcher)
    staff_plugin.register(dispatcher, api_id, api_hash)
    sudo_plugin.register(dispatcher, api_id, api_hash)
    userinfo_plugin.register(dispatcher, api_id, api_hash)
    welcome_plugin.register(dispatcher, api_id, api_hash)