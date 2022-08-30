from celery import shared_task
from django.core.mail import send_mail


def generate_activation_code(self):
        from django.utils.crypto import get_random_string
        code = get_random_string(length=8, allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
        self.activation_code = code 
        self.save()

@shared_task
def send_activation_code(self):
        generate_activation_code()
        activation_url = f'http://127.0.0.1:8000/account/activate/{self.activation_code}'
        message = f'Активируйте свой аккаунт пройдя по этой ссылке {activation_url}'
        send_mail('Активация аккаунта', message, 'cars@gmail.com', [self.email])


