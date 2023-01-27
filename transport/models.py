from django.db.models import Model, CharField, PositiveIntegerField, DateField, DecimalField


char_kwargs = {'max_length': 200}
decimal_kwargs = {'decimal_places': 2, 'max_digits': 9}


class Transport(Model):
    make = CharField(**char_kwargs)
    model = CharField(**char_kwargs)
    year = PositiveIntegerField()
    service_interval = PositiveIntegerField()
    next_service = DateField()

    class Meta:
        abstract = True


class Car(Transport):
    seats = PositiveIntegerField()
    color = CharField(**char_kwargs)
    VIN = CharField(**char_kwargs, unique=True)
    current_mileage = DecimalField(**decimal_kwargs)


class Truck(Transport):
    seats = PositiveIntegerField()
    color = CharField(**char_kwargs)
    bed_length = DecimalField(**decimal_kwargs)
    VIN = CharField(**char_kwargs, unique=True)
    current_mileage = DecimalField(**decimal_kwargs)


class Boat(Transport):
    length = DecimalField(**decimal_kwargs)
    width = DecimalField(**decimal_kwargs)
    HIN = CharField(**char_kwargs)
    current_hours = DecimalField(**decimal_kwargs)
