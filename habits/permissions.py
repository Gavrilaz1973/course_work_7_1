from rest_framework.permissions import BasePermission


class IsOwnerOrStaff(BasePermission):
    """
        Пользователь (модератор) может редактировать и удалять свои привычки.
    """

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        if request.user == obj.user:
            return True
        return False