from rest_framework import serializers
from . import models
from apps.resources.serializers.imported_serializers import ResourceModelSerializer


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = "__all__"


class UserUpdateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        exclude = ("username", "password")


class UserProfileModelSerializer(serializers.ModelSerializer):
    resources = ResourceModelSerializer(source="resources_set", many=True)

    class Meta:
        model = models.User
        fields = ("id", "username", "first_name", "last_name", "resources")
