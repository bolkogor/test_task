from django.db.models import Model, CharField, PositiveIntegerField, DateField, DecimalField


class Transport(Model):
    make = CharField(max_length=200)
    model = CharField(max_length=200)
    year = PositiveIntegerField()
    service_interval = PositiveIntegerField()
    next_service = DateField()

    class Meta:
        abstract = True


class Car(Transport):
    seats = PositiveIntegerField()
    color = CharField(max_length=200)
    VIN = CharField(max_length=200)
    current_mileage = DecimalField(decimal_places=2, max_digits=9)


class Truck(Transport):
    seats = PositiveIntegerField()
    color = CharField(max_length=200)
    bed_length = DecimalField(decimal_places=2, max_digits=6)
    VIN = CharField(max_length=200)
    current_mileage = DecimalField(decimal_places=2, max_digits=9)


class Boat(Transport):
    length = DecimalField(decimal_places=2, max_digits=9)
    width = DecimalField(decimal_places=2, max_digits=6)
    NIH = CharField(max_length=200)
    current_hours = DecimalField(decimal_places=2, max_digits=9)
