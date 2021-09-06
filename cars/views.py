from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from cars.models import Car
from cars.serializers import CarSerializer


class CarsViewSet(APIView):
    def get(self, *args, **kwargs):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

