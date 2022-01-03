import re
import random
from datetime import datetime
from sched import scheduler

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger

import requests
from lxml import html
from telegram import Bot
from telegram.ext import Updater, CommandHandler

scheduler = BlockingScheduler()

file = open("token.token", 'r')
token = file.read()


@scheduler.scheduled_job(IntervalTrigger(seconds=7))
def sendMessageToChannel():
    bot = Bot(token)
    bot.send_message("@linkedinfars", "this message sent from boy")


if __name__ == '__main__':
    scheduler.start()
