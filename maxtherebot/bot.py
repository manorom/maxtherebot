from datetime import timedelta, datetime
from telegram.ext import CommandHandler
from telegram import ParseMode

from .maxthere import max_there_state


def paypallink_callback(update, context):
    update.message.reply_text('Max denkt [das hier ist der link zum Paypal MoneyPool](https://www.paypal.com/pools/c/80WwEOPFZl)',
                              quote=True, disable_web_page_preview=True,
                              parse_mode=ParseMode.MARKDOWN)

def maxthere_callback(update, context):
    last_seen = max_there_state.last_seen()
    if datetime.now() - last_seen < timedelta(minutes=5):
        update.message.reply_text('Ich hab Max in den letzten 5 Minuten noch gesehen')
    elif datetime.now() - last_seen < timedelta(minutes=10):
        update.message.reply_text('Ich hab Max in den letzten 10 Minuten noch gesehe')
    else:
        update.message.reply_text('Ich glaube Max ist nicht da.')


def help_callback(update, context):
    update.message.reply_text('Mit dem Befehl /max kann ich dir sagen wann ich Max zuletzt im Keller gesehen habe.')


def configure_dispatcher(dispatcher):
    dispatcher.add_handler(CommandHandler('help', help_callback))
    dispatcher.add_handler(CommandHandler('max', maxthere_callback))
    dispatcher.add_handler(CommandHandler('paypal', paypallink_callback))
