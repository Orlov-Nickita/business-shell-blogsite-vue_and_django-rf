from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework import status
from rest_framework.response import Response

from blogs_app.models import Post, Comment
from blogs_app.serializers import PostCreateSerializer, PostListSerializer, PostDetailSerializer, \
    CommentCreateSerializer


class PostCreateAPIView(CreateAPIView):
    serializer_class = PostCreateSerializer
    queryset = Post.objects.all()
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            a = serializer.save()
            return Response(f'Успешно добавлен новый пост - id = {a.id}', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# curl -X POST http://127.0.0.1:8000/api/post/create/ -H "Content-Type: application/json" -d "{\"author\":1, \"title\":\"this is first post in the blog site\", \"description\":\"this is description of the first post\"}"

class PostListAPIView(ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def get_queryset(self):
        post_id = self.kwargs.get('post_id', None)
        qs = super().get_queryset()
        
        if post_id:
            self.serializer_class = PostDetailSerializer
            return qs.filter(id=post_id)
        
        return qs


class CommentCreateAPIView(CreateAPIView):
    serializer_class = CommentCreateSerializer
    queryset = Comment.objects.all()
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Комментарий успешно добавлен', status=status.HTTP_201_CREATED)
