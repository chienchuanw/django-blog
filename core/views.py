from django.views.generic import TemplateView
from typing import Any
from posts.models import Post


class HomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        posts = Post.objects.all().order_by("-pk")

        # Sorted tags in each post
        for post in posts:
            post.sorted_tags = post.tags.all().order_by("name")

        context["posts"] = posts

        return context
