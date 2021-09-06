from rest_framework import serializers

from cars.models import Car, CarRate

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'make', 'model', 'avg_rating')

class CarSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('make', 'model')

class CarRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarRate
        fields = ('car_id', 'rating')