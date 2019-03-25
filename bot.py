#!/usr/bin/env python
# Copyright (c) 2019 Steepo
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

# -*- coding: utf-8 -*-
import logging
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import datetime 
from pathlib import Path

# slugify
import unicodedata
import re

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger("RedBullBot")

def start(bot, update):
    """Send a message when the command /start is issued."""  
    logger.info(f"Start issued by: {get_user_name(update.message.from_user)}")
    update.message.reply_text('Ciao, mandami una foto mentre bevi una Red Bull', quote=True)


def help(bot, update):
    """Send a message when the command /help is issued."""
    logger.info(f"Help issued by: {get_user_name(update.message.from_user)}")
    update.message.reply_text('Mandami una foto mentre bevi una Red Bull', quote=True)


def slugify(value, allow_unicode=False):
    """
    https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces to hyphens.
    Remove characters that aren't alphanumerics, underscores, or hyphens.
    Convert to lowercase. Also strip leading and trailing whitespace.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value).strip().lower()
    return re.sub(r'[-\s]+', '-', value)

def get_user_name(user):
    name = None
    if user.username:
        name = user.username
    else:
        name = user.first_name
        if user.last_name:
            name = f"{name} {user.last_name}"
    return name

def save_photo(bot, update):
    logger.info(f"Photo sent by: {get_user_name(update.message.from_user)}")
    file_id = update.message.photo[-1].file_id
    photo = bot.get_file(file_id)
    update.message.reply_text("Grazie per la foto, goditi la tua Red Bull!", quote=True)
    timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    valid_user_name = slugify(get_user_name(update.message.from_user))
    filename = f"{timestamp}_{valid_user_name}_{update.message.message_id}.png"
    photo.download(Path(f"./pic/{filename}"))

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.error(f'Update "{update}" caused error "{error}"')

def main():
    """Start the bot."""
    logger.info("The bot is starting...")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    if BOT_TOKEN is None:
        logger.critical("Please set the BOT_TOKEN env variable")
        return 

    updater = Updater(BOT_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # photo handler
    dp.add_handler(MessageHandler(Filters.photo, save_photo))

    dp.add_error_handler(error)

    logger.info("The bot is listening...")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
