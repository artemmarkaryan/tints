import requests
from django.conf import settings
from urllib.parse import quote


def make_url(phones, message):
    return f"https://smsc.ru/sys/send.php?login={settings.SMS_LOGIN}" \
           f"&psw={settings.SMS_PASSWORD}" \
           f"&phones={phones}&mes={quote(message)}&fmt=3" \
           f"&charset=utf-8" \
           f"&sender=TON"


def send(phones, message):
    r = requests.get(make_url(phones, message))
    print(phones, message, r.text)
    return r.text
