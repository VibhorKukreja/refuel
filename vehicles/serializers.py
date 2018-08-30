from rest_framework import serializers

from . import models


class VehicleSerializer(serializers.ModelSerializer):
    """A serializer for our profile object."""

    class Meta:
        model = models.Vehicle
        fields = ('__all__')


class FuelSerializer(serializers.ModelSerializer):
    """A serializer for our profile object."""

    class Meta:
        model = models.Fuel
        fields = ('__all__')
