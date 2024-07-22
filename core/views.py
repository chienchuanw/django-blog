from django.views.generic import TemplateView, View
from typing import Any
from posts.models import Post
from django.shortcuts import render


class HomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        posts = Post.objects.all().order_by("-pk")

        for post in posts:
            # Sorted tags in each post
            post.sorted_tags = post.tags.all().order_by("name")

        context["posts"] = posts

        return context


class AboutView(TemplateView):
    template_name = "core/about.html"


class Custom404View(View):
    def get(self, request, exception=None):
        return render(request, "errors/404.html")
