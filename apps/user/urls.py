from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.user_list, name="user-list"),
    path("login/", views.login_view, name="login-view"),
    path("profile/", views.profile, name="profile"),
]
