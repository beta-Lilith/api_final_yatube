from rest_framework import permissions


NOT_ALLOWED_TO_CHANGE = 'У вас нет разрешения редактировать эту запись.'


class IsAuthorOrReadOnly(permissions.BasePermission):
    message = NOT_ALLOWED_TO_CHANGE

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
