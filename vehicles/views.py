from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authentication import TokenAuthentication

from rest_framework import viewsets, filters

from . import serializers, models, permissions


class VehiclesViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profiles."""

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnVehicle,)
    serializer_class = serializers.VehicleSerializer
    queryset = models.Vehicle.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('fuel_type', 'model',)


class FuelsViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profiles."""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.FuelSerializer
    queryset = models.Fuel.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('fuel_type', 'quantity', 'amount')
