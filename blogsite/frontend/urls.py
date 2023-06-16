from django.urls import path
from django.views.generic import TemplateView

app_name = 'frontend'

urlpatterns = [
    path('', TemplateView.as_view(template_name='frontend/index.html'), name='index'),
    path('post/<int:post_id>/', TemplateView.as_view(template_name='frontend/post_detail.html'), name='post_detail'),
    path('post/create/', TemplateView.as_view(template_name='frontend/post_create.html'), name='post_create'),
    path('users/registration/', TemplateView.as_view(template_name='frontend/registration.html'), name='registration'),
]
