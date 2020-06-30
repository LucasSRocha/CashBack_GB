from rest_framework.permissions import BasePermission


class IsAdminOrOwner(BasePermission):
    """
    Allow access to admin users or the user himself.
    """

    def has_object_permission(self, request, view, obj):
        if request.user and (request.user.is_staff or request.user.is_superuser):
            return True
        elif request.user == obj.user:
            return True
        return False
