from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from cars.models import Car, CarRate
from cars.serializers import CarSerializer, CarSerializerPost, CarRatingSerializer, PopularCarsSerializer
from utils import connector
from utils.rating_validator import rating_validator


class CarsViewSet(APIView):
    def get(self, *args, **kwargs):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, *args, **kwargs):
        validate = connector.Connector(
            car_make=request.data.get('make'),
            car_model=request.data.get('model')
        ).get_data()

        if validate:
            serializer = CarSerializerPost(data=request.data, many=False)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"Error": "Car not found!"}, status=status.HTTP_204_NO_CONTENT)


class CarDetailView(generics.RetrieveDestroyAPIView):
    queryset = Car
    serializer_class = CarSerializer


class CarRatesSet(APIView):
    def post(self, request, *args, **kwargs):

        try:
            rating = int(request.data.get("rating"))
            rating = rating_validator(rating)
            car = Car.objects.get(id=request.data.get("car_id"))
        except Car.DoesNotExist:
            return Response({"error": "Object doesn't exist!"}, status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            return Response({"rating": "This field should be an integer"}, status=status.HTTP_400_BAD_REQUEST)
        cars = CarRate.objects.create(car_id=car, rating=rating)
        serializer = CarRatingSerializer(cars, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PopularCarsSet(APIView):
    def get(self, *args, **kwargs):
        cars = Car.objects.all()
        if cars:
            serializer = PopularCarsSerializer(cars, many=True)
            serializer_data = sorted(serializer.data, key=lambda k: k['rates_number'], reverse=True)
            return Response(serializer_data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
