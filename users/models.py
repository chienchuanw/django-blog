from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="userprofile_set",
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="userprofile_set",
        blank=True,
    )

    def __str__(self):
        return self.username
