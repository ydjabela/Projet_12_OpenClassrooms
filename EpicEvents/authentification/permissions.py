from rest_framework.permissions import BasePermission
from authentification.models import User
import logging
logger = logging.getLogger("EpicEvents")


class ClientPermissions(BasePermission):
    message = "You do not have access"

    def has_permission(self, request, view):
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        if user.role == "sales_member":
            return True
        elif user.role == "support_member":
            if view.action == 'create' or view.action == 'update':
                logger.warning("You do not have access")
                return False
            else:
                return True
        elif user.role == "management_member":
            return True
        else:
            logger.warning("You do not have access")
            return False


class UserPermissions(BasePermission):
    message = "You do not have access"

    def has_permission(self, request, view):
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        if user.role == "management_member":
            return True
        else:
            logger.warning("You do not have access")
            return False
