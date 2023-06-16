from django.contrib import admin

from blogs_app.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Класс для настроек и отображения в админ панели модели Post
    """
    list_display = ['title', 'description', 'author', 'published_at']
    list_display_links = ['title', 'description']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Класс для настроек и отображения в админ панели модели Comment
    """
    list_display = ['comment', 'post', 'author', 'published_at']
    list_display_links = ['comment', 'post']