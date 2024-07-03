from django.db import models
from users.models import CustomUser
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255, blank=False)
    content = models.TextField(blank=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        tags = ", ".join(f"#{tag.name}" for tag in self.tags.all())
        return f"{self.title} ({tags})"

    def publish(self):
        self.published_at = timezone.now()
        self.save()
