from rest_framework import permissions


class IsWorker(permissions.BasePermissions):
    def has_permission(self, request, view):
        pass
