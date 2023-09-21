from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home-page"),
    path("resource/<int:id>", views.resources_detail, name="resources-detail"),
    path("resource/post/", views.resource_post, name="resource-post"),
]
