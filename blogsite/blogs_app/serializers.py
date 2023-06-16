from rest_framework import serializers
from blogs_app.models import Comment, Post
from users.serializers import UserDetailSerializer


class CommentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Comment для метода GET
    """
    published_at = serializers.DateTimeField(read_only=True, format="%H:%M %d-%m-%Y")
    author = UserDetailSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = ['author', 'comment', 'published_at']


class CommentCreateSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Comment для метода POST
    """
    comment = serializers.CharField(max_length=None, required=True)
    
    class Meta:
        model = Comment
        fields = ['author', 'comment', 'post']


class PostCreateSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Post для метода POST
    """
    description = serializers.CharField(max_length=None, required=True)
    
    class Meta:
        model = Post
        fields = ['title', 'description', 'author']


class PostDetailSerializer(serializers.ModelSerializer):
    """
        Сериализатор для модели Post для метода GET
        """
    id = serializers.IntegerField(read_only=True)
    author = UserDetailSerializer(read_only=True)
    published_at = serializers.DateTimeField(read_only=True, format="%H:%M %d-%m-%Y")
    comments = CommentSerializer(read_only=True, many=True)
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'author', 'published_at', 'href', 'comments']
