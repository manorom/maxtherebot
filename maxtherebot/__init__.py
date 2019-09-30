import os

from . import maxthere
from telegram.ext import Updater
from .bot import configure_dispatcher

def cli():
    maxthere.patch_webhook()
    telegram_token = os.environ['TELEGRAM_TOKEN']
    maxthere_token = os.environ['MAXTHERE_TOKEN']
    maxthere.max_token = maxthere_token
    updater = Updater(telegram_token)
    configure_dispatcher(updater.dispatcher)
    port = 80
    local_urlpath = telegram_token
    updater.start_webhook(listen="127.0.0.1", port=port, url_path=local_urlpath)
    updater.idle()