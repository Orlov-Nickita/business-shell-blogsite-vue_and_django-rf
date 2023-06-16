from django.urls import path

from users.views import RegistrationAPIView

app_name = 'users'

urlpatterns = [
    path('registration/', RegistrationAPIView.as_view(), name='registration'),
]
