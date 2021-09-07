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


class PopularCarsSerializer(serializers.ModelSerializer):

    rates_number = serializers.SerializerMethodField("get_rates_number")

    def get_rates_number(self, car):
        rates_number = CarRate.objects.filter(car_id=car).count()
        return rates_number

    class Meta:
        model = Car
        fields = ('id', 'make', 'model', 'rates_number')
