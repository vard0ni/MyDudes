from rest_framework import serializers
from .models import Profile
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        ref_name = 'ProfileUser'
        exclude = (
            "password",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions",
            "last_login"
        )


class GetUserSerializer(serializers.ModelSerializer):
    """ Вывод инфо о user
    """
    #avatar = serializers.ImageField(read_only=True)
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ('user', 'first_name', 'last_name', 'avatar', 'birthday', 'gender', 'hobbies', 'verified')


class GetUserPublicSerializer(serializers.ModelSerializer):
    """ Вывод публичной инфы о user
    """
    #user = UserSerializer()

    class Meta:
        model = Profile
        fields = ('id', 'first_name', 'last_name', 'avatar', 'birthday', 'gender', 'hobbies', 'verified')
