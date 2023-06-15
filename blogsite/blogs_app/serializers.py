from django.contrib.auth.models import User
from rest_framework import serializers

from blogs_app.models import Comment, Post


class UseShortSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели User
    """
    
    class Meta:
        """
        Метакласс для определения модели и полей модели, с которыми будет работать сериализатор
        """
        model = User
        fields = ['username']


class UserDetailSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели User
    """
    
    class Meta:
        """
        Метакласс для определения модели и полей модели, с которыми будет работать сериализатор
        """
        model = User
        fields = ['username', 'first_name', 'last_name']


class CommentSerializer(serializers.ModelSerializer):
    published_at = serializers.DateTimeField(read_only=True, format="%H:%M %d-%m-%Y")
    author = UserDetailSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = ['author', 'comment', 'published_at']


class CommentCreateSerializer(serializers.ModelSerializer):
    comment = serializers.CharField(max_length=None, required=True)
    
    class Meta:
        model = Comment
        fields = ['author', 'comment', 'post']


class PostCreateSerializer(serializers.ModelSerializer):
    description = serializers.CharField(max_length=None, required=True)
    
    class Meta:
        model = Post
        fields = ['title', 'description', 'author']


class PostListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    author = UseShortSerializer(read_only=True)
    published_at = serializers.DateTimeField(read_only=True, format="%H:%M %d-%m-%Y")
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'author', 'published_at']
    
    def to_representation(self, instance):
        a = super().to_representation(instance)
        a['author'] = a['author']['username']
        return a


class PostDetailSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    author = UserDetailSerializer(read_only=True)
    published_at = serializers.DateTimeField(read_only=True, format="%H:%M %d-%m-%Y")
    comments = CommentSerializer(read_only=True, many=True)
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'author', 'published_at', 'comments']
