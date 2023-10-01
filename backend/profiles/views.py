from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .models import Profile
from .serializers import GetUserSerializer, GetUserPublicSerializer


class UserPublicView(ModelViewSet):
    """ Вывод публичного профиля пользователя
    """

    # извлекаем все объекты модели Profile из базы данных
    queryset = Profile.objects.all()
    serializer_class = GetUserPublicSerializer
    # Endpoint доступен всем юзерам, включая анонимных
    permission_classes = [permissions.AllowAny]


class UserView(ModelViewSet):
    """ Вывод профиля пользователя
    """
    serializer_class = GetUserSerializer
    # Endpoint доступен только авторизованным пользователям
    permission_classes = [permissions.IsAuthenticated]

    # извлекается только профиль текущего зарегистрированного и аутентифицированного пользователя
    def get_queryset(self):
        return Profile.objects.filter(id=self.request.user.id)
