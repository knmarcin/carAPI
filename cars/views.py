from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from cars.models import Car
from cars.serializers import CarSerializer, CarSerializerPost
from utils import connector


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
            return Response({"Error":"Car not found!"}, status=status.HTTP_204_NO_CONTENT)


class CarDetailView(generics.RetrieveDestroyAPIView):
    queryset = Car
    serializer_class = CarSerializer

class CarRatesSet(APIView):
    def post(self, request, *args, **kwargs):
        rating = request.data.get("rating")




