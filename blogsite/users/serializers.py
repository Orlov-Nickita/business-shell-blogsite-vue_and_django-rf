from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class UserDetailSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели User для метода GET
    """
    class Meta:
        """
        Метакласс для определения модели и полей модели, с которыми будет работать сериализатор
        """
        model = User
        fields = ['username', 'first_name', 'last_name']


class UserCreateSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели User для метода POST
    """
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']
        write_only_fields = ['password']
        read_only_fields = ['id']
    
    def validate_password(self, value):
        validate_password(value)
        return value
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        
        return user


class SetPasswordSerializer(serializers.Serializer):
    """
    Сериализатор для создания пароля и проверки двух паролей на идентичность
    """
    password = serializers.CharField(required=True)
    passwordReply = serializers.CharField(required=True)
    
    def validate(self, attrs):
        """
        Валидация присланных в форме паролей.
        :param attrs: Содержит пароли из отправленной формы.
        :return: Возвращает массив с паролями или поднимает исключение о не совпадении.
        """
        if attrs.get('password') != attrs.get('passwordReply'):
            raise ValidationError("Пароли не совпадают")
        return attrs