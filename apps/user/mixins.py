from .serializers import serializers


class RestrictInactivateUsersMixin:
    def get_serializer_class(self):
        if not self.request.user.is_active:
            return serializers.UserUpdateModelSerializer
        else:
            return serializers.UserModelSerializer
