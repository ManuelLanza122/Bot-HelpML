from telegram import ParseMode
from telegram.ext import CommandHandler, MessageHandler, Filters
from functools import wraps
import register_plugins


def register(dispatcher, api_id, api_hash):
    dispatcher.add_handler(CommandHandler('afk', set_afk))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, check_afk))


# Decorador para verificar si el usuario está marcado como AFK
def afk_check(func):
    @wraps(func)
    def wrapped(update, context):
        user = update.effective_user
        if user and user.is_authenticated:
            user_data = context.user_data
            if 'afk' in user_data:
                message = f"{user.username} está ausente: {user_data['afk']}"
                send_media(context.bot, update.effective_chat.id, message, user_data.get('media'))
        return func(update, context)
    return wrapped


# Comando para establecer el estado de AFK
def set_afk(update, context):
    user_data = context.user_data
    if len(context.args) > 0:
        afk_message = " ".join(context.args)
        media = extract_media_from_message(context.args)
        user_data['afk'] = afk_message
        user_data['media'] = media
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"{update.effective_user.username} está ahora ausente: {afk_message}", parse_mode=ParseMode.MARKDOWN)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Debes proporcionar un mensaje para establecer tu estado AFK.")


# Función para verificar si se menciona a un usuario AFK
@afk_check
def check_afk(update, context):
    pass


# Función para enviar contenido multimedia cuando se menciona a un usuario AFK
def send_media(bot, chat_id, message, media):
    if media is None:
        bot.send_message(chat_id=chat_id, text=message, parse_mode=ParseMode.MARKDOWN)
    elif media.startswith('photo:'):
        photo_url = media.replace('photo:', '')
        bot.send_photo(chat_id=chat_id, photo=photo_url, caption=message, parse_mode=ParseMode.MARKDOWN)
    elif media.startswith('video:'):
        video_url = media.replace('video:', '')
        bot.send_video(chat_id=chat_id, video=video_url, caption=message, parse_mode=ParseMode.MARKDOWN)
    elif media.startswith('sticker:'):
        sticker_id = media.replace('sticker:', '')
        bot.send_sticker(chat_id=chat_id, sticker=sticker_id)
    elif media.startswith('audio:'):
        audio_url = media.replace('audio:', '')
        bot.send_audio(chat_id=chat_id, audio=audio_url, caption=message, parse_mode=ParseMode.MARKDOWN)


# Función para extraer el contenido multimedia de un mensaje
def extract_media_from_message(args):
    for arg in args:
        if arg.startswith('photo:') or arg.startswith('video:') or arg.startswith('sticker:') or arg.startswith('audio:'):
            return arg
    return None


register_plugins.register_plugin(register)