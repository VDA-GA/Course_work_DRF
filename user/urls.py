from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenRefreshView

from user.apps import UserConfig
from user.views import (MyTokenObtainPairView, UserCreateAPIView, UserDestroyAPIView, UserListAPIView,
                        UserRetrieveAPIView, UserUpdateAPIView)

app_name = UserConfig.name

urlpatterns = [
    path("login/", MyTokenObtainPairView.as_view(permission_classes=[AllowAny]), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(permission_classes=[AllowAny]), name="token_refresh"),
    path("register/", UserCreateAPIView.as_view(), name="user_register"),
    path("list/", UserListAPIView.as_view(), name="users_list"),
    path("<int:pk>/", UserRetrieveAPIView.as_view(), name="user_detail"),
    path("update/<int:pk>/", UserUpdateAPIView.as_view(), name="user_update"),
    path("delete/<int:pk>/", UserDestroyAPIView.as_view(), name="user_delete"),
]
