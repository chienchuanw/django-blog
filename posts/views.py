from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import *
from .forms import *


class PostListView(ListView):
    pass


def post_list(request):
    return render(request, "posts/list.html")


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "posts/create.html"
    login_url = reverse_lazy("users:login")
    success_url = reverse_lazy("posts:list")
