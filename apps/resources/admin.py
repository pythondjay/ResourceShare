from django.contrib import admin
from apps.resources import models


# Register your models here.
class CustomResources(admin.ModelAdmin):
    list_display = (
        "username",
        "user_title",
        "title",
        "link",
        "all_tags",
        "description",
    )

    @admin.display(description="Tags")
    def get_tags(self, obj):
        return ",".join([tag.name for tag in self.tag.all()])


class CustomRating(admin.ModelAdmin):
    list_display = ("get_username", "get_resource_title", "rate")

    @admin.display(description="username")
    def get_username(self, obj):
        return obj.user_id.username

    @admin.display(description="resource title")
    def get_resource_title(self, obj):
        return obj.resources_id.title


class CustomReview(admin.ModelAdmin):
    list_display = ("username", "title", "body")


admin.site.register(models.Tag)
admin.site.register(models.Category)
admin.site.register(models.Resources, CustomResources)
admin.site.register(models.Review, CustomReview)
admin.site.register(models.Rating, CustomRating)
admin.site.register(models.ResourcesTag)
