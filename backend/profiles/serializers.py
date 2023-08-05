from rest_framework import serializers
from .models import Profile


class GetUserSerializer(serializers.ModelSerializer):
    """ Вывод инфо о user
    """
    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'


class GetUserPublicSerializer(serializers.ModelSerializer):
    """ Вывод публичной инфы о user
    """

    class Meta:
        model = Profile
        fields = '__all__'
