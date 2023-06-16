from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    """
    Модель Пост
    """
    title = models.CharField(max_length=100, verbose_name='Заголовок поста')
    description = models.TextField(null=False, verbose_name='Текст поста')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор поста')
    published_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    
    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
    
    def __str__(self):
        return f'Пост: {self.title}'
    
    def href(self):
        """
        Возвращает ссылку на объект модели Пост
        """
        return f'post/{self.id}/'


class Comment(models.Model):
    """
    Модель Комментарий
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария')
    comment = models.TextField(null=False, verbose_name='Комментарий')
    published_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания комментария')
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, verbose_name='Пост')
    
    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'

    def __str__(self):
        return f'Комментарий: {self.comment}'