from django.views.generic import TemplateView
from typing import Any
from posts.models import Post


class HomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context