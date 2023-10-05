from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Resources, Category
from .serializers import serializers
from . import mixins
from . import permissions


@api_view(["GET"])
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def list_resources(request):
    queryset = (
        Resources.objects.select_related("user_id", "cat_id")
        .prefetch_related("tag")
        .all()
    )

    # response = [
    # {
    # "title": query.title,
    # "links": query.link,
    # "user": {
    # "id": query.user_id.id,
    # "username": query.user_id.username,
    # },
    # "category": query.cat_id.cat,
    # "tags": query.all_tags(),
    # }
    # for query in queryset
    # ]

    response = serializers.ResourceModelSerializer(queryset, many=True)
    # transform to JSON before returning
    return Response(response.data)


@api_view(["GET"])
def list_category(request):
    categories = Category.objects.all()
    # response = [
    # {
    # "id": query.id,
    # "name": query.cat,
    # }
    # for query in categories
    # ]
    response = serializers.CategorySerializer(categories, many=True)
    # transform to JSON before returning
    return Response(response.data)


class ListResource(ListAPIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = (
        Resources.objects.select_related("user_id", "cat_id")
        .prefetch_related("tag")
        .all()
    )
    serializer_class = serializers.ResourceModelSerializer


class ListCategory(ListAPIView):
    categories = Category.objects.all()
    serializer_class = serializers.CategoryModelSerializer


class DetailResource(RetrieveAPIView):
    lookup_field = "id"  # by default the lookup field is pk
    queryset = (
        Resources.objects.select_related("user_id", "cat_id")
        .prefetch_related("tag")
        .all()
    )
    serializer_class = serializers.ResourceModelSerializer


# ViewSets can permit us to perform the CRUD operations in one class based view.


class ResourceViewSets(viewsets.ModelViewSet):
    permission_classes = (permissions.AuthorSuperOrReadOnly,)
    permission_classes = (permissions.TwoWeeksOldObjectSuperOnly,)
    queryset = (
        Resources.objects.select_related("user_id", "cat_id")
        .prefetch_related("tag")
        .all()
    )
    serializer_class = serializers.ResourceModelSerializer


class CategoryViewSets(
    mixins.DenyDeletionOfDefaultCategoryMixin, viewsets.ModelViewSet
):
    permission_classes = (permissions.AuthorSuperOrReadOnly,)
    queryset = Category.objects.all()
    serializer_class = serializers.CategoryModelSerializer


class DeleteCategory(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategoryModelSerializer
