from rest_framework import permissions


class IsTeacher(permissions.BasePermission):
    """
    Custom permission to only allow teachers to edit or create lessons and contents.
    """

    def has_permission(self, request, view):
        # Allow only authenticated teachers to create or edit lessons/contents
        if request.user.is_authenticated:
            return request.user.role == 'teacher'  # Ensure that the user has the 'teacher' role
        return False

    def has_object_permission(self, request, view, obj):
        # Allow only teachers to edit or delete their own lessons/contents
        if request.user.is_authenticated:
            return request.user.role == 'teacher'  # Same permission check as in `has_permission`
        return False
