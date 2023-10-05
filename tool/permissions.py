from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

class IsLoggedIn(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

class IsAuthenticatedForSwagger(IsAuthenticated):
    def has_permission(self, request, view):
        if view.__class__.__name__ == "SpectacularAPIView":
            return request.user and request.user.is_authenticated
        return super().has_permission(request, view)