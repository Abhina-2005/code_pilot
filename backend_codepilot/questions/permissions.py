from rest_framework.permissions import BasePermission

class Owneronly(BasePermission) :

    def has_object_permission(self, request, view, obj):
        return request.assessment.creator == obj.user