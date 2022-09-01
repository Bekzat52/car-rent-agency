from rest_framework import serializers
from cars.models import Car, Category, Like, Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        exclude = ['id']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ['id']

class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ['id']

class CarDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Car
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['category'] = CategorySerializer(instance.category).data
        rep['ratings'] = instance.get_average_rating
        return rep


class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        # fields = '__all__'
        fields = ('id','category', 'mark', 'model', 'user', 'likes')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['category'] = CategorySerializer(instance.category).data
        rep['user'] = instance.user.email
        rep['rating'] = instance.get_average_rating
        rep["likes"] = instance.likes.all().count()
        rep['liked_by_user'] = False
        rep["user_rating"] = 0
        
        request = self.context.get('request')

        if request.user.is_authenticated:
            rep['liked_by_user'] = Like.objects.filter(user = request.user, product=instance).exists()
            if Rating.objects.filter(user=request.user, product=instance).exists():
                rating = Rating.objects.get(user=request.user, product=instance)
                rep["user_rating"] = rating.value

        return rep
