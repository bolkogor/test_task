from rest_framework.viewsets import ModelViewSet
from .serializers import CarSerializer, TruckSerializer, BoatSerializer
from .models import Car, Boat, Truck


class CarViewSet(ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class BoatViewSet(ModelViewSet):
    serializer_class = BoatSerializer
    queryset = Boat.objects.all()


class TruckViewSet(ModelViewSet):
    serializer_class = TruckSerializer
    queryset = Truck.objects.all()
