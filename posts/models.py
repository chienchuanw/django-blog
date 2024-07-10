from django.db import models
from users.models import CustomUser
from django.utils import timezone
from django.utils.text import slugify
from markdownx import models as mdx_models


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name="Tag name")

    class Meta:
        verbose_name = "Post Tag"
        verbose_name_plural = "Post Tags"

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255, blank=False)
    content = mdx_models.MarkdownxField(blank=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name="posts")
    slug = models.SlugField(blank=True, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        tags = ", ".join(f"#{tag.name}" for tag in self.tags.all())
        return f"{self.title} ({tags})"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def publish(self):
        self.published_at = timezone.now()
        self.save()


class Image(models.Model):
    image = models.ImageField(upload_to="posts/images/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
