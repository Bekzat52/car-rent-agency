from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from cars.serializer import *
from cars.models import Car



# class CarAPIListPagination(PageNumberPagination):
#     page_size = 5
#     page_size_query_param = 'page_size'
#     max_page_size = 10000

class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer

class CarListView(generics.ListAPIView):
    serializer_class = CarListSerializer
    queryset = Car.objects.all()
    # pagination_class = CarAPIListPagination

class CarDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
    # permission_classes = ...