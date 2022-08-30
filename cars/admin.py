from django.contrib import admin
from .models import Car, Category, Like, Rating


admin.site.register(Category)
admin.site.register(Car)
admin.site.register(Like)
admin.site.register(Rating)