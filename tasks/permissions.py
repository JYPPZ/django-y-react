from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Permiso personalizado para permitir solo a los dueños de un objeto editarlo.
    """
    def has_object_permission(self, request, view, obj):
        # (GET, HEAD, OPTIONS) se permiten a cualquier usuario autenticado.
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user