from django.contrib import admin
from django.urls import path, include
from cars.views import *



urlpatterns = [
    path('create/', CarCreateView.as_view()),
    path('all_list/', CarListView.as_view()),
    path('detail/<int:pk>/', CarDetailView.as_view()),
]