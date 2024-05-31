from django.shortcuts import render
from django.views.generic import ListView


class PostListView(ListView):
    pass


def post_list(request):
    return render(request, "posts/list.html")
