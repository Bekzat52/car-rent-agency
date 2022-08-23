from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

CAR_TYPES = (
    ('Sedan', 'Sedan'),
    ('Hatchback', 'Hatchback'),
    ('Minivan', 'Minivan'),
    ('Coupe', 'Coupe'),
)

MARK = (
    ('Audi','Audi'),
    ('Mercedes-Benz','Mercedes-Benz'),
    ('Toyota','Toyota'),
    ('Honda','Honda'),
    ('Nissan','Nissan'),
)

HAND = (
    ('LEFT','Left'),
    ('RIGHT','Right'),
)

class Car(models.Model):
    mark = models.CharField(verbose_name="Марка", choices=MARK, max_length=50)
    model = models.CharField(verbose_name="Модель", max_length=30)
    body = models.CharField(verbose_name="Кузов", choices=CAR_TYPES, max_length=50)
    color = models.CharField(verbose_name="Цвет", max_length=30)
    hand = models.CharField(verbose_name="Руль", choices=HAND, max_length=50)
    engine = models.FloatField(verbose_name="Обьем пример:1,8")
    image = models.ImageField()
    price = models.DecimalField(verbose_name="Цена", max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, blank=True, verbose_name='Пользователь', on_delete=models.CASCADE)
