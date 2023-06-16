from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.response import Response
from blogs_app.models import Post, Comment
from blogs_app.serializers import PostCreateSerializer, PostDetailSerializer, \
    CommentCreateSerializer


class PostCreateAPIView(CreateAPIView):
    """
    Представление для создания постов
    """
    serializer_class = PostCreateSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAdminUser]
    
    def post(self, request, *args, **kwargs):
        data = {
            'title': request.data.get('post_title'),
            'description': request.data.get('post_description'),
            'author': request.user.id,
        }
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostListAPIView(ListAPIView):
    """
    Представление для получения всех постов из БД
    """
    serializer_class = PostDetailSerializer
    queryset = Post.objects.order_by('-published_at').all()
    permission_classes = [AllowAny]
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def get_queryset(self):
        post_id = self.kwargs.get('post_id', None)
        qs = super().get_queryset()
        
        if post_id:
            return qs.filter(id=post_id)
        
        return qs


class CommentCreateAPIView(CreateAPIView):
    """
    Представление для создания комментариев
    """
    serializer_class = CommentCreateSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        data = {
            'author': request.user.id,
            **request.data
        }
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
