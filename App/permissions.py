from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.role == "Admin"
            or request.user.is_staff
        )


class IsAdminOrManagerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(
            request.user
            and request.user.role == "Admin"
            or request.user.role == "Manager"
            or request.user.is_staff
        )


class IsAdminOrManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.role == "Admin"
            or request.user.role == "Manager"
            or request.user.is_staff
        )
