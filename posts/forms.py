from django.forms import ModelForm
from .models import *


class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]


class PostUpdateForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "tag"]
