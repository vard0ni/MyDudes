from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .models import Profile
from .serializers import GetUserSerializer, GetUserPublicSerializer


class UserPublicView(ModelViewSet):
    """ Вывод публичного профиля пользователя
    """
    queryset = Profile.objects.all()
    serializer_class = GetUserPublicSerializer
    permission_classes = [permissions.AllowAny]


class UserView(ModelViewSet):
    """ Вывод профиля пользователя
    """
    serializer_class = GetUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Profile.objects.filter(id=self.request.user.id)
