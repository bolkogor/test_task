from rest_framework import serializers
from .models import Car, Boat, Truck

transport_fields = ['id', 'make', 'model', 'year', 'service_interval', 'next_service']


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [
            *transport_fields,
            'seats',
            'current_mileage',
            'VIN',
            'color'
        ]


class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = [
            *transport_fields,
            'seats',
            'current_mileage',
            'VIN',
            'color',
            'bed_length'
        ]


class BoatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boat
        fields = [
            *transport_fields,
            'length',
            'width',
            'HIN',
            'current_hours',
        ]
