from rest_framework import generics
from cars.serializer import *
from cars.models import Car



class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer

class CarListView(generics.ListAPIView):
    serializer_class = CarListSerializer
    queryset = Car.objects.all()

class CarDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
    permission_classes = ...