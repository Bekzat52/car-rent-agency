from django.contrib import admin
from .models import Car, Category, Like, Rating


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'category', 'engine', 'price']
    list_editable = ['category', 'engine', 'price']
    ordering = ['price']
    list_per_page = 20
    search_fields = ['mark','model']
    list_filter = ['price']
    

admin.site.register(Category)
admin.site.register(Like)
admin.site.register(Rating)

