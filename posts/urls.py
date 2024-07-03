from django.urls import path
from .views import PostCreateView, PostUpdateView, PostListView, PostDetailView

app_name = "posts"

urlpatterns = [
    path("", PostListView.as_view(), name="list"),
    path("create/", PostCreateView.as_view(), name="create"),
    path("<int:pk>/update", PostUpdateView.as_view(), name="update"),
    path("<int:pk>/", PostDetailView.as_view(), name="detail"),
]
