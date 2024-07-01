from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import *
from .forms import *


class PostListView(ListView):
    pass


def post_list(request):
    posts = Post.objects.all()
    return render(request, "posts/list.html", {"posts": posts})


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = "posts/create.html"
    login_url = reverse_lazy("users:login")
    success_url = reverse_lazy("posts:list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = "posts/update.html"
    success_url = reverse_lazy("posts:list")

    def get_object(self):
        post = get_object_or_404(Post, pk=self.kwargs["pk"])
        return post

    def form_valid(self, form):
        messages.success(self.request, "更新成功")
        return super().form_valid(form)
