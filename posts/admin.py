from django.contrib import admin
from .models import Post, Tag
from markdownx.admin import MarkdownxModelAdmin


class PostAdmin(MarkdownxModelAdmin, admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
