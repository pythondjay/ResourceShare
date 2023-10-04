from rest_framework.exceptions import PermissionDenied

DEFAULT_CATEGORY_ID = 1


class DenyDeletionOfDefaultCategoryMixin:
    # This is the method to use for Listing
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action == "destroy":  # because of view sets
            pk = self.kwargs["pk"]
            deleted_queryset = queryset.get(pk=pk)
            if deleted_queryset.pk == DEFAULT_CATEGORY_ID:
                raise PermissionDenied(f"Not allowed to delete a category with id {pk}")
        # Never forget
        return queryset

    def destroy(self, request, *args, **kwargs):
        pass


class FilterOutAdminResourcesMixin:
    def get_queryset(self):
        queryset = super().get_queryset().exclude(user_id_is_superuser__exact=True)
        return queryset
