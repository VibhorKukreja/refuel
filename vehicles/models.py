from django.db import models

# Create your models here.

VEHICLE_TYPE = (
        ('BIKE', 'Bike'),
        ('CAR', 'Car'),
    )

FUEL_TYPE = (
        ('PETROL', 'Petrol'),
        ('DIESEL', 'Diesel'),
    )


class Vehicle(models.Model):

    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=15)
    engine_capacity = models.IntegerField()
    user_profile = models.ForeignKey('users.UserProfile', on_delete=models.CASCADE)
    vehicle_type = models.CharField(
        max_length=10,
        choices=VEHICLE_TYPE,
        default='BIKE',
    )
    fuel_type = models.CharField(
        max_length=10,
        choices=FUEL_TYPE,
        default='PETROL',
    )

    def __str__(self):
        return '{} - {} - {}'.format(self.brand, self.model, self.registration_number)


class Fuel(models.Model):

    vehicle_id = models.ForeignKey('Vehicle', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    amount = models.IntegerField()
    transaction_date = models.DateTimeField(auto_now_add=True)
    fuel_type = models.CharField(
        max_length=10,
        choices=FUEL_TYPE,
        default='PETROL',
    )
    autocomplete_fields = ['fuel_type']

    def __str__(self):
        return '{} - {} - {}'.format(self.fuel_type, self.vehicle_id, self.quantity)