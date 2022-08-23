from django.contrib import admin
from django.urls import path, include
from cars.views import *



urlpatterns = [
    path('car/create/', CarCreateView.as_view()),
    path('car/all_list/', CarListView.as_view()),
    path('car/detail/<int:pk>/', CarDetailView.as_view()),
]