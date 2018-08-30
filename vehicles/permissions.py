from rest_framework import permissions


class UpdateOwnVehicle(permissions.BasePermission):
    """
    Only allow users to edit their own profile.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id