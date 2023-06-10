from telegram import InputTextMessageContent, InlineQueryResultArticle, ParseMode
from telegram.ext import CommandHandler, InlineQueryHandler
from uuid import uuid4

welcome_image_url = 'https://example.com/bienvenida.jpg'  # URL de la imagen de bienvenida
welcome_message = "¡Saludos, aventurero! Soy un bot épico creado para brindarte asistencia en tus travesías. ¡Prepárate para embarcarte en una experiencia increíble! 💪🔥"

def register(dispatcher, api_id, api_hash, owner_id):
    def start(update, context):
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=welcome_image_url, caption="¡Bienvenido! 🎉")
        context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_message)

    def set_image(update, context):
        if update.effective_user.id != owner_id:
            context.bot.send_message(chat_id=update.effective_chat.id, text="¡No tienes permisos para ejecutar este comando!")
            return

        new_image_url = context.args[0] if context.args else None
        global welcome_image_url
        welcome_image_url = new_image_url
        context.bot.send_message(chat_id=update.effective_chat.id, text="¡La imagen de bienvenida ha sido actualizada!")

    def set_message(update, context):
        if update.effective_user.id != owner_id:
            context.bot.send_message(chat_id=update.effective_chat.id, text="¡No tienes permisos para ejecutar este comando!")
            return

        new_message = ' '.join(context.args) if context.args else None
        global welcome_message
        welcome_message = new_message
        context.bot.send_message(chat_id=update.effective_chat.id, text="¡El mensaje de bienvenida ha sido actualizado!")

    def inline_start(update, context):
        query = update.inline_query.query
        title = "Bot de Bienvenida"
        if query.strip() == '':
            message = f"<b>Información de Bienvenida:</b>\n\n"
            message += f"<b>Imagen:</b> <a href='{welcome_image_url}'>&#8205;</a>\n"
            message += f"<b>Mensaje:</b> {welcome_message}"
            context.bot.answer_inline_query(
                inline_query_id=update.inline_query.id,
                results=[
                    InlineQueryResultArticle(
                        id=uuid4(),
                        title=title,
                        input_message_content=InputTextMessageContent(message, parse_mode=ParseMode.HTML),
                        description="Bienvenida personalizada"
                    )
                ]
            )

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('set_image', set_image))
    dispatcher.add_handler(CommandHandler('set_message', set_message))
    dispatcher.add_handler(InlineQueryHandler(inline_start))