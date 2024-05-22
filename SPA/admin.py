from django.contrib import admin

from SPA.models import Habit


@admin.register(Habit)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "action",
        "user",
        "place",
        "time",
        "is_pleasant",
        "frequency",
        "linked_habit",
        "reward",
        "action_time",
        "is_published",
    ]
