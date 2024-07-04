from django.views.generic import TemplateView
from typing import Any
from posts.models import Post
from markdown import Markdown


class HomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        posts = Post.objects.all().order_by("-pk")

        for post in posts:
            # Sorted tags in each post
            post.sorted_tags = post.tags.all().order_by("name")

            # Convert markdown content to HTML
            md = Markdown(extensions=["fenced_code"])
            post.content = md.convert(post.content)

        context["posts"] = posts

        return context
