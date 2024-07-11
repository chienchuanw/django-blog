from django.db import models
from users.models import CustomUser
from django.utils import timezone
from django.utils.text import slugify
from markdownx import models as mdx_models
from PIL import Image as PIL_Image
import io
from django.core.files.uploadedfile import InMemoryUploadedFile


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
    image = models.ImageField(upload_to="posts/images/", verbose_name="Image Name")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def compress_image(self, upload_image):
        # Open image to load and check the picture info
        image = PIL_Image.open(upload_image)

        if image.format != "WEBP" or upload_image.size > 100 * 1024:
            # Compress and convert image
            image_io = io.BytesIO()
            image.save(image_io, format="WEBP", quality=90)

            # Rename image file extension to .webp
            new_image = InMemoryUploadedFile(
                image_io, None, f"{upload_image.name.split(".")[0]}.webp", "image/webp", image_io.getbuffer().nbytes, None
            )
            return new_image
        return upload_image

    def save(self, *args, **kwargs):
        # Compress image if it exists
        if self.image:
            self.image = self.compress_image(self.image)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"


class Video(models.Model):
    video = models.FileField(upload_to="posts/videos", verbose_name="Video Name")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "videos"
