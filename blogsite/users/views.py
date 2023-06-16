from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from users.serializers import UserCreateSerializer, SetPasswordSerializer


class RegistrationAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        passwords = {
            'password': request.data.get('password'),
            'passwordReply': request.data.pop('passwordReply'),
        }
        pass_serializer = SetPasswordSerializer(data=passwords)
        if pass_serializer.is_valid(raise_exception=True):
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid(raise_exception=True):
                user = serializer.save()
                login(request, user)
                return Response(status=status.HTTP_201_CREATED)
            return Response(data=serializer.errors, status=status.HTTP_200_OK)
        return Response(data=pass_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
