from unicodedata import category
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from cars.serializer import *
from cars.models import Car, Like, Rating
from rest_framework.generics import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view


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

class CategoryCreateView(generics.CreateAPIView):
    serializer_class = CategorySerializer

class CategoryDetailView(generics.DestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

@api_view(['GET'])
def toggle_like(request, p_id):
    user = request.user
    product = get_object_or_404(Car, id=p_id)

    if Like.objects.filter(user=user, product=product).exists():
       Like.objects.filter(user=user, product=product).delete()
    else:
        Like.objects.create(user=user, product=product)
    
    return Response('Like toggled', 200)


@api_view(["POST"])
def add_rating(request, p_id):
    user = request.user
    product = get_object_or_404(Car, id=p_id)
    value = request.POST.get("value")

    if not user.is_authenticated:
        raise ValueError("authentication credentials are not provided")

    if not value:
        raise ValueError("value is required")
    
    if Rating.objects.filter(user=user, product=product).exists():
        rating = Rating.objects.get(user=user, product=product)
        rating.value = value
        rating.save()
    else:
        Rating.objects.create(user=user, product=product, value=value)
    
    return Response("rating created", 201)