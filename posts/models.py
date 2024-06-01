from django.db import models
from users.models import *
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=255, blank=False)
    content = models.TextField(blank=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    tag = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    def publish(self):
        self.published_at = timezone.now()
        self.save()
