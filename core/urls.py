from django.contrib import admin
from django.urls import path, include
from .views import HomeView, Custom404View
from django.conf import settings
from django.conf.urls import handler404

handler404 = Custom404View.as_view()

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path(settings.ADMIN_URL, admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("markdownx/", include("markdownx.urls")),
    path("users/", include("users.urls")),
    path("posts/", include("posts.urls")),
]
