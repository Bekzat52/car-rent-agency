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

class Category(models.Model):
    title = models.CharField(verbose_name="Категория", max_length=50)

    def __str__(self):
        return f"{self.title}"


class Car(models.Model):
    category = models.ForeignKey(Category, verbose_name="Категория", related_name='categories', on_delete=models.CASCADE)
    mark = models.CharField(verbose_name="Марка", choices=MARK, max_length=50)
    model = models.CharField(verbose_name="Модель", max_length=30)
    body = models.CharField(verbose_name="Кузов", choices=CAR_TYPES, max_length=50)
    color = models.CharField(verbose_name="Цвет", max_length=30)
    hand = models.CharField(verbose_name="Руль", choices=HAND, max_length=50)
    engine = models.FloatField(verbose_name="Обьем пример:1,8")
    image = models.ImageField()
    price = models.DecimalField(verbose_name="Цена", max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, blank=True, verbose_name='Пользователь', on_delete=models.CASCADE)

    @property
    def get_average_rating(self):
        ratings = [rating.value for rating in self.ratings.all()]
        if ratings:
            return sum(ratings) / len(ratings)
        return 0

    def __str__(self):
        return f'{self.mark} {self.model}'

class Rating(models.Model):
    user = models.ForeignKey(User, related_name='ratings', on_delete=models.CASCADE)
    product = models.ForeignKey(Car, related_name='ratings', on_delete=models.CASCADE)
    value = models.IntegerField(choices=[(1,1), (2,2), (3,3), (4,4), (5,5)])
    

class Like(models.Model):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    product = models.ForeignKey(Car, related_name='likes', on_delete=models.CASCADE)