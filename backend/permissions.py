from rest_framework import permissions
from .models import Manager, Fridge, User

class IsManagerOf(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            userId = User.objects.filter(username=request.user)[0].id
            fridgeId = Fridge.objects.filter(name=obj)[0].id
            p = Manager.objects.filter(user__id=userId).filter(fridge__id=fridgeId)
            return bool(p)

class IsAdminUserOrReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in permissions.SAFE_METHODS or is_admin