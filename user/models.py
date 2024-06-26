from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="email")
    phone = models.CharField(max_length=35, **NULLABLE, verbose_name="номер телефона")
    avatar = models.ImageField(upload_to="users/", **NULLABLE, verbose_name="аватарка")
    city = models.CharField(max_length=100, **NULLABLE, verbose_name="город")
    chat_id = models.CharField(max_length=50, **NULLABLE, verbose_name="chat_id_tg")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
