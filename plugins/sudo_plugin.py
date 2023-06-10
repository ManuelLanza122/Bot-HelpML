from telegram.ext import CommandHandler
import os
from register_plugin import register_plugin

def register(dispatcher, api_id, api_hash):
    # Define la función de manejo para el comando "/sudo"
    def sudo(update, context):
        # Obtiene el ID del remitente del mensaje
        user_id = update.effective_user.id

        # Obtiene el ID del propietario del bot desde las variables de entorno
        owner_id = int(os.getenv('OWNER_ID'))

        # Verifica si el remitente es el propietario del bot o un "sudo" autorizado
        if user_id == owner_id or user_id in context.bot_data.get('sudo_users', []):
            # Realiza acciones especiales aquí
            context.bot.send_message(chat_id=update.effective_chat.id, text="¡Acción especial realizada!")
        else:
            # Si el remitente no tiene permisos, envía un mensaje de error
            context.bot.send_message(chat_id=update.effective_chat.id, text="¡No tienes permisos para ejecutar este comando!")

    # Registra el comando "/sudo" con la función de manejo
    dispatcher.add_handler(CommandHandler('sudo', sudo))

def addsudo(user_id, bot_data):
    # Añade un usuario como "sudo" autorizado
    sudo_users = bot_data.get('sudo_users', [])
    if user_id not in sudo_users:
        sudo_users.append(user_id)
        bot_data['sudo_users'] = sudo_users
        return True
    return False

def remsudo(user_id, bot_data):
    # Elimina un usuario de la lista de "sudo" autorizados
    sudo_users = bot_data.get('sudo_users', [])
    if user_id in sudo_users:
        sudo_users.remove(user_id)
        bot_data['sudo_users'] = sudo_users
        return True
    return False

register_plugin