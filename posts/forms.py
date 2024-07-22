from django import forms
from .models import Post, Image, Video


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ["image"]


class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ["video"]


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "tags"]
