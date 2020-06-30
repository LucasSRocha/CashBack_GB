from rest_framework.permissions import BasePermission


class IsAdminOrSelf(BasePermission):
    """
    Allow access to admin users or the user himself.
    """

    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_staff or request.user.is_superuser:
            return True
        elif request.user and type(obj) == type(request.user) and obj == request.user:
            return True
        return False


class AnonCreateUser(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated or view.action == "create":
            return True
        return False
