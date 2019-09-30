from datetime import timedelta, datetime
from telegram.ext import CommandHandler

from .maxthere import max_last_seen


def maxthere_callback(update, context):
    last_seen = max_last_seen()
    if datetime.now() - last_seen < timedelta(minutes=5):
        update.reply_text('Ich hab Max vor 5 Minuten noch gesehen')
    if datetime.now() - last_seen < timedelta(minutes=10):
        update.reply_text('Ich hab Max vor 10 Minuten noch gesehe')
    else:
        update.reply_text('Ich glaube Max ist nicht da.')


def help_callback(update, context):
    update.reply_text('Mit dem Befehl /max kann dir sagen wann Max mir zuletzt gemeldet hat, dass er im Keller ist.')


def configure_dispatcher(dispatcher):
    dispatcher.add_handler(CommandHandler('help', help_callback))
    dispatcher.add_handler(CommandHandler('max', maxthere_callback))

