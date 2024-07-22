from django.contrib import admin
from django.urls import path, include
from .views import HomeView, Custom404View, AboutView
from django.conf import settings
from django.conf.urls import handler404
from django.conf.urls.static import static
from django.shortcuts import render


def nav(request):
    return render(request, "shared/base.html")


handler404 = Custom404View.as_view()

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path(settings.ADMIN_URL, admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("markdownx/", include("markdownx.urls")),
    path("users/", include("users.urls")),
    path("posts/", include("posts.urls")),
    path("nav/", nav),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
