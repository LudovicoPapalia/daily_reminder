# daily_reminder
A telegram bot that every day send you a notification if you have to do something important. If you haven't clicked the "done" button it resend it again. Your status is notified to another user

the code updated to march 2023 (latest update) is in the file "code1"

It is provided "as is". the programmer is NOT responsible for the use you will make of it.

The project is made for personal and educational purposes and may not be updated in case of library changes. Any use you make of the code is your full and complete responsibility. The author is not responsible for any action or damage caused to people, animals or things (including damage to your computer or possible bans from platforms such as telegram)

The project was written in Italian and the comments are in Italian. The variables are in English to be easily understood. You are free to translate the comments if you like

With this code, the bot sends a notification every N time. The notification is sent to user A. If user a does not click the button, I will enter. given time N1, both user A and user B are notified. The notification is automatically resend after the passage of time N. The notifications contain the counter of how many days the bot has worked, how many notifications it has sent in total and how many in a day.

The libraries used are:

import logging

import telegram

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

import datetime

import threading
