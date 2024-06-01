from django.urls import path
from .views import *

app_name = "posts"

urlpatterns = [
    # path("", PostListView.as_view(), name="list"),
    path("", post_list, name="list"),
    path("create/", PostCreateView.as_view(), name="create"),
    path("update/", update, name="update"),
]
