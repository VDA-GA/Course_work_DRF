from datetime import datetime, timedelta

import pytz
from celery import shared_task
from django.conf import settings

from SPA.models import Habit
from SPA.services import send_tg_message


@shared_task
def send_tg_message_to_user():
    zone = pytz.timezone(settings.TIME_ZONE)
    today = zone.localize(datetime.now()).replace(second=0, microsecond=0)
    habits = Habit.objects.filter(time__lte=today)
    for habit in habits:
        message = f"Выполни действие: {habit.action}"
        chat_id = habit.user.chat_id
        if chat_id:
            send_tg_message(chat_id, message)
        habit.time += timedelta(days=habit.frequency)
        habit.save()
