from datetime import datetime, timezone

from celery import shared_task

from SPA.models import Habit
from SPA.services import send_tg_message


@shared_task
def send_tg_message_to_user():
    today = datetime.now(timezone.utc)
    habits = Habit.objects.filter(time__lte=today)
    for habit in habits:
        message = f'Выполни действие: {habit.action}'
        chat_id = habit.user.get('chat_id')
        if chat_id:
            send_tg_message(chat_id, message)
        habit.time += habit.frequency
        habit.save()
