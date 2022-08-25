from rest_framework import generics
from cars.serializer import *
from cars.models import Car, Like
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404




class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer

class CarListView(generics.ListAPIView):
    serializer_class = CarListSerializer
    queryset = Car.objects.all()

class CarDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
    permission_classes = ...


@api_view(['GET'])
def toggle_like(request, p_id):
    user = request.user
    product = get_object_or_404(Car, id=p_id)

    if Like.objects.filter(user=user, product=product).exists():
       Like.objects.filter(user=user, product=product).delete()
    else:
        Like.objects.create(user=user, product=product)
    
    return Response('Like toggled', 200)