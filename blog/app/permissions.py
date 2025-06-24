from rest_framework.permissions import BasePermission,SAFE_METHODS
class AccessByOwnership(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            if request.user == obj.blog_writer:
                return True
            else:
                return False