from telegram import InputTextMessageContent, InlineQueryResultArticle, ParseMode
from telegram.ext import CommandHandler, InlineQueryHandler
from uuid import uuid4

def register(dispatcher, api_id, api_hash):
    dispatcher.add_handler(CommandHandler('userinfo', userinfo))
    dispatcher.add_handler(InlineQueryHandler(inline_userinfo))

def userinfo(update, context):
    user = update.effective_user
    message = f"ID: {user.id}\n"
    message += f"Nombre: {user.first_name}\n"
    message += f"Apellido: {user.last_name}\n"
    message += f"Nombre de usuario: {user.username}\n"

    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def inline_userinfo(update, context):
    query = update.inline_query.query
    user = update.effective_user

    if user.id == owner_id or user.id in sudo_users:
        title = "Usuario Sudo"
    else:
        title = "Usuario"

    if query.strip() == '':
        bio = user.bio or 'N/A'
        message = f"<b>Información del {title}:</b>\n\n"
        message += f"<b>ID:</b> {user.id}\n"
        message += f"<b>Nombre:</b> {user.first_name}\n"
        message += f"<b>Apellido:</b> {user.last_name}\n"
        message += f"<b>Nombre de usuario:</b> @{user.username}\n"
        message += f"<b>Biografía:</b> {bio}"

        context.bot.answer_inline_query(
            inline_query_id=update.inline_query.id,
            results=[
                InlineQueryResultArticle(
                    id=uuid4(),
                    title=title,
                    input_message_content=InputTextMessageContent(message, parse_mode=ParseMode.HTML)
                )
            ]
        )

# Resto del código del plugin

from register_plugin import owner_id, sudo_users