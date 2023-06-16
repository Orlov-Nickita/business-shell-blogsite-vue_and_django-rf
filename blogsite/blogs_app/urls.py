from django.urls import path
from blogs_app.views import PostCreateAPIView, PostListAPIView, CommentCreateAPIView

app_name = 'blogs_app'

urlpatterns = [
    path('post/create/', PostCreateAPIView.as_view(), name='post_create'),
    path('post/', PostListAPIView.as_view(), name='post_list'),
    path('post/<int:post_id>/', PostListAPIView.as_view(), name='post_detail'),
    path('comment/create/', CommentCreateAPIView.as_view(), name='comment_create'),
]
