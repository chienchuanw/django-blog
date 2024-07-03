from django.contrib import admin
from django.urls import path, include
from .views import HomeView
from django.conf import settings

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path(settings.ADMIN_URL, admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("users/", include("users.urls")),
    path("posts/", include("posts.urls")),
]
