from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=100, blank=True)
    birth_date = models.DateTimeField(null=True, blank=True)
    avatar = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.username
