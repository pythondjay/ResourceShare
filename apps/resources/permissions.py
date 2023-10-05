from datetime import timedelta, timezone
from rest_framework import permissions


class AuthorSuperOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # Superuser is okay
        if request.user.is_superuser:
            return True

        # GET /api/v1/resource/1
        if request.method in permissions.SAFE_METHODS:
            return True

        # check if the authenticated user is the author of the resource
        if request.user.id == obj.user_id.id:
            return True

        return False


class TwoWeeksOldObjectSuperOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        two_weeks_ago = timezone.now() - timedelta(weeks=2)
        if obj.created_at < two_weeks_ago:
            if request.user.is_superuser:
                return True
            else:
                return False
        return True
