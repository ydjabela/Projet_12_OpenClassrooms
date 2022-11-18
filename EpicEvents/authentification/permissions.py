from rest_framework.permissions import BasePermission
from authentification.models import Client, User


class ClientPermissions(BasePermission):
    message = "You do'nt have not acces"

    def has_permission(self, request, view):
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        if user.role == "sales_member":
            return True
        elif user.role == "support_member":
            if view.action == 'create' or view.action == 'update':
                return False
            else:
                return True
        elif user.role == "management_member":
            return True
        else:
            return False


class UserPermissions(BasePermission):
    message = "You do'nt have not acces"

    def has_permission(self, request, view):
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        if user.role == "management_member":
            return True
        else:
            return False

