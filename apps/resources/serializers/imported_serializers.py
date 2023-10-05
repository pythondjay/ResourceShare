from rest_framework import serializers
from .. import models


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = (
            "id",
            "cat",
        )


class TagModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = (
            "id",
            "name",
        )


class ResourceModelSerializer(serializers.ModelSerializer):
    cat_id = CategoryModelSerializer()
    tag = TagModelSerializer(many=True)

    class Meta:
        model = models.Resources
        # two options
        # specify the fields we want our serializer to serialize
        # omit fields that our serializer shouldn't serialize
        fields = (
            "id",
            "title",
            "description",
            "link",
            "cat_id",
            "tag",
        )
