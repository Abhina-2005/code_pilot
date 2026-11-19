<<<<<<< HEAD
from rest_framework.permissions import BasePermission

from assessment.models import Assessment

class OwnerOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user==obj.creator
=======


>>>>>>> 3985fa0 (Updated backend)
