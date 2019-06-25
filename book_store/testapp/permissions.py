from rest_framework.permissions import BasePermission, SAFE_METHODS

class ChandanPermission(BasePermission):
    message = 'You must be the author of the application'
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
                return True
        return request.user.is_staff
