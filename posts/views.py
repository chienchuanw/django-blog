from typing import Any
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, FormView
from .models import Post
from .forms import PostCreateForm, PostUpdateForm, ImageUploadForm


class PostListView(ListView):
    model = Post
    template_name = "posts/list.html"
    context_object_name = "posts"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all().order_by("-pk")
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = "posts/create.html"
    login_url = reverse_lazy("users:login")
    success_url = reverse_lazy("posts:list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@method_decorator(csrf_exempt, name="dispatch")
class ImageUploadView(FormView):
    form_class = ImageUploadForm

    def form_invalid(self, form: Any) -> HttpResponse:
        return JsonResponse({"error": "Image upload failed"}, status=400)

    def form_valid(self, form):
        image = form.save()
        return JsonResponse({"url": image.image.url})


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


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        post = self.get_object()

        # Sorted tags in each post
        context["sorted_tags"] = post.tags.all().order_by("name")

        return context
