from django.contrib import admin

from blogs_app.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'author', 'published_at']
    list_display_links = ['title', 'description']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment', 'post', 'author', 'published_at']
    list_display_links = ['comment', 'post']