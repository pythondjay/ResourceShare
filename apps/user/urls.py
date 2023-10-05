from django.urls import path
from . import views
from . import api_views


api_urlpatterns = [
    path("api/v1/login/", api_views.UserLogin.as_view(), name="user-login-class"),
    path("api/v1/profile/", api_views.UserProfile.as_view(), name="user-profile-class"),
]

urlpatterns = [
    path("list/", views.user_list, name="user-list"),
    path("login/", views.login_view, name="login-view"),
    path("profile/", views.profile, name="profile"),
    *api_urlpatterns,
    # path("update/<int:id>/", views.UpdateUser.as_view(), name="update-user"),
]
