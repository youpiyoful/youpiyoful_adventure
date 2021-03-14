from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    To authenticate users and ensure that only the
    owner of a post can update or delete an existing post
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user
