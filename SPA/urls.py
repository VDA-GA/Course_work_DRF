from django.urls import path

from SPA.apps import SpaConfig
from SPA.views import (HabitCreateAPIView, HabitDestroyAPIView, HabitPublishedListAPIView, HabitRetrieveAPIView,
                       HabitUpdateAPIView, HabitUserListAPIView)

app_name = SpaConfig.name

urlpatterns = [
    path("habit/create/", HabitCreateAPIView.as_view(), name="create_habit"),
    path("habit/user_list/", HabitUserListAPIView.as_view(), name="user_habits"),
    path("habit/published_list/", HabitPublishedListAPIView.as_view(), name="published_habits"),
    path("habit/<int:pk>/", HabitRetrieveAPIView.as_view(), name="habit_detail"),
    path("habit/update/<int:pk>/", HabitUpdateAPIView.as_view(), name="habit_update"),
    path("habit/delete/<int:pk>/", HabitDestroyAPIView.as_view(), name="habit_delete"),
]
