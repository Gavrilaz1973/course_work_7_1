from datetime import datetime

import requests
from celery import shared_task
from django.utils import timezone

from config import settings
from habits.models import Habit


@shared_task
def print_message():
    TOKEN = settings.TEL_TOKEN
    current_time = datetime.now().time()
    for habit in Habit.objects.all():
        if habit.time.hour == current_time.hour and habit.time.minute == current_time.minute:
            chat_id = habit.user.telegram_id      #'5383568164'
            message = f"Пора выполнить привычку: {habit.action}"
            url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
            # print(chat_id, message, habit.time, current_time)
            requests.post(url)
    # #
    # # return response.json()
