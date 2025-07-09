# cliente/permissions.py
from rest_framework import permissions

class SoloSuperuserPuedeCrear(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.is_superuser
        return True  
