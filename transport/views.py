from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import CarSerializer, TruckSerializer, BoatSerializer
from .models import Car, Boat, Truck


class TransportViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]


class CarViewSet(TransportViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class BoatViewSet(TransportViewSet):
    serializer_class = BoatSerializer
    queryset = Boat.objects.all()


class TruckViewSet(TransportViewSet):
    serializer_class = TruckSerializer
    queryset = Truck.objects.all()
