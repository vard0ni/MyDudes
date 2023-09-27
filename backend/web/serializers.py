from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator

User = get_user_model()


class UserRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    phone = serializers.CharField(max_length=15, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['email'],
            email=validated_data['email'],
            phone=validated_data['phone'],
            password=validated_data['password']
        )


class UserLoginSerializer(serializers.Serializer):
    email_phone = serializers.CharField()
    password = serializers.CharField(write_only=True)
