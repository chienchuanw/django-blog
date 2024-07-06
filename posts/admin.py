from django.contrib import admin
from .models import Post, Tag


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
