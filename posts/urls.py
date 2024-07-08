from django.urls import path
from .views import (
    PostCreateView,
    PostUpdateView,
    PostListView,
    PostDetailView,
    ImageUploadView,
)

app_name = "posts"

urlpatterns = [
    path("", PostListView.as_view(), name="list"),
    path("create/", PostCreateView.as_view(), name="create"),
    path("<slug:slug>/update/", PostUpdateView.as_view(), name="update"),
    path("<slug:slug>/", PostDetailView.as_view(), name="detail"),
    path("image/upload/", ImageUploadView.as_view(), name="image_upload"),
]
