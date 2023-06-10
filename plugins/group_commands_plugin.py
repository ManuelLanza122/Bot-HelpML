from telegram import ChatPermissions
from telegram.ext import CommandHandler, Filters
import os
import register_plugins

def register(dispatcher, api_id, api_hash):
    # Define las funciones de manejo para los comandos
    dispatcher.add_handler(CommandHandler('kick', kick, filters=Filters.group & Filters.user(api_id)))
    dispatcher.add_handler(CommandHandler('ban', ban, filters=Filters.group & Filters.user(api_id)))
    dispatcher.add_handler(CommandHandler('unban', unban, filters=Filters.group & Filters.user(api_id)))
    dispatcher.add_handler(CommandHandler('mute', mute, filters=Filters.group & Filters.user(api_id)))
    dispatcher.add_handler(CommandHandler('unmute', unmute, filters=Filters.group & Filters.user(api_id)))
    dispatcher.add_handler(CommandHandler('promote', promote, filters=Filters.group & Filters.user(api_id)))
    dispatcher.add_handler(CommandHandler('demote', demote, filters=Filters.group & Filters.user(api_id)))
    dispatcher.add_handler(CommandHandler('pin', pin, filters=Filters.group & Filters.user(api_id)))
    dispatcher.add_handler(CommandHandler('unpin', unpin, filters=Filters.group & Filters.user(api_id)))

def kick(update, context):
    # Lógica para ejecutar el comando de kick
    user_id = extract_user_id_from_command(update.message.text)
    if user_id:
        context.bot.kick_chat_member(chat_id=update.effective_chat.id, user_id=user_id)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Usuario expulsado del grupo")

def ban(update, context):
    # Lógica para ejecutar el comando de ban
    user_id = extract_user_id_from_command(update.message.text)
    if user_id:
        context.bot.ban_chat_member(chat_id=update.effective_chat.id, user_id=user_id)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Usuario baneado del grupo")

def unban(update, context):
    # Lógica para ejecutar el comando de unban
    user_id = extract_user_id_from_command(update.message.text)
    if user_id:
        context.bot.unban_chat_member(chat_id=update.effective_chat.id, user_id=user_id)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Usuario desbaneado del grupo")

def mute(update, context):
    # Lógica para ejecutar el comando de mute
    user_id = extract_user_id_from_command(update.message.text)
    if user_id:
        context.bot.restrict_chat_member(chat_id=update.effective_chat.id, user_id=user_id, permissions=ChatPermissions(can_send_messages=False))
        context.bot.send_message(chat_id=update.effective_chat.id, text="Usuario silenciado en el grupo")

def unmute(update, context):
    # Lógica para ejecutar el comando de unmute
    user_id = extract_user_id_from_command(update.message.text)
    if user_id:
        context.bot.restrict_chat_member(chat_id=update.effective_chat.id, user_id=user_id, permissions=ChatPermissions(can_send_messages=True))
        context.bot.send_message(chat_id=update.effective_chat.id, text="Usuario desilenciado en el grupo")

def promote(update, context):
    # Lógica para ejecutar el comando de promote
    user_id = extract_user_id_from_command(update.message.text)
    if user_id:
        context.bot.promote_chat_member(chat_id=update.effective_chat.id, user_id=user_id, can_change_info=True, can_delete_messages=True, can_invite_users=True, can_restrict_members=True, can_pin_messages=True, can_promote_members=False)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Usuario promovido en el grupo")

def demote(update, context):
    # Lógica para ejecutar el comando de demote
    user_id = extract_user_id_from_command(update.message.text)
    if user_id:
        context.bot.promote_chat_member(chat_id=update.effective_chat.id, user_id=user_id, can_change_info=False, can_delete_messages=False, can_invite_users=False, can_restrict_members=False, can_pin_messages=False, can_promote_members=False)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Usuario degradado en el grupo")

def pin(update, context):
    # Lógica para ejecutar el comando de pin
    message_id = extract_message_id_from_command(update.message.text)
    if message_id:
        context.bot.pin_chat_message(chat_id=update.effective_chat.id, message_id=message_id)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Mensaje anclado en el grupo")

def unpin(update, context):
    # Lógica para ejecutar el comando de unpin
    context.bot.unpin_all_chat_messages(chat_id=update.effective_chat.id)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Todos los mensajes desanclados del grupo")
