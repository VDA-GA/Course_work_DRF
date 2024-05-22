import requests
from django.conf import settings


def send_tg_message(chat_id, message):
    params = {"text": message, "chat_id": chat_id}
    url = f"https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}/sendMessage"
    requests.get(url, params=params)
