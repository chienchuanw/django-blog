from django.urls import path
from .views import PostCreateView, PostUpdateView, PostListView

app_name = "posts"

urlpatterns = [
    path("", PostListView.as_view(), name="list"),
    path("create/", PostCreateView.as_view(), name="create"),
    path("<int:pk>/update", PostUpdateView.as_view(), name="update"),
]
