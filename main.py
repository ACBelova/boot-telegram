from tracemalloc import start
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

from bot_commande import *



updater = Updater('5162327352:AAGah3i2gm9AQB9uFSBkmnTQtdggrBxvKx4')

updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('joke', joke_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))



print('server start')
updater.start_polling()
updater.idle()

