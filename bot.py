#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import os
import datetime 

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger("RedBullBot")

def start(bot, update):
    """Send a message when the command /start is issued."""  
    logger.info(update.message.from_user.id)
    update.message.reply_text('Ciao, mandami una foto mentre bevi una Redbull', quote=True)


def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Mandami una foto mentre bevi una RedBull', quote=True)


def tgphoto(bot, update):
    file_id = update.message.photo[-1].file_id
    newFile = bot.get_file(file_id)
    update.message.reply_text("Grazie per la foto, goditi la tua RedBull", quote=True)
    print(update)
    now = datetime.datetime.now()
    timeStamp = now.strftime('%d_%m_%Y_%H-%M')
    fileName = str(update.message.from_user.username)+ "_" + str(timeStamp)+ str(update.message.message_id)+'.png'
    newFile.download("./pic/"+fileName)

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

def main():
    """Start the bot."""
    token = os.environ.get("BOT_TOKEN")
    if token is None:
        logger.critical("Please set the BOT_TOKEN env variable")
        return 

    updater = Updater(token)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # photo handler
    dp.add_handler(MessageHandler(Filters.photo, tgphoto))

    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
