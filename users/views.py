from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authentication import TokenAuthentication

from rest_framework import viewsets, filters

from . import serializers, models
from . import permissions


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profiles."""

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class LoginViewSet(viewsets.ViewSet):
    """Handles creating and returning user authentication tokens."""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Check the email and password and return an auth token."""

        return ObtainAuthToken().post(request)
