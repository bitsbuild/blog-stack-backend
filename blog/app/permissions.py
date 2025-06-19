from rest_framework import permissions
class ReviewPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            if obj.review_writer == request.user:
                return True
            else:
                return False
class BlogPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            if obj.blog_writer == request.user:
                return True
            else:
                return False