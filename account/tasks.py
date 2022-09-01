from celery import shared_task
from django.core.mail import send_mail
from django.dispatch import receiver
from django.urls import reverse
from password_reset.signals import reset_password_token_created

@shared_task
def send_code(activation_code, email):
    activation_url = f'http://127.0.0.1:8000/account/activate/{activation_code}'
    message = f'Активируйте свой аккаунт пройдя по этой ссылке {activation_url}'
    send_mail('Активация аккаунта', message, 'cars@gmail.com', [email])
    return "send"

