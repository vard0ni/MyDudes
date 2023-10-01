from rest_framework import generics, permissions, views, response
from profiles.models import User
from .models import Follower
from .serializers import ListFollowerSerializer


# generics.ListAPIView обрабатывает HTTP GET запросы для вывода списка подписчиков
class ListFollowerView(generics.ListAPIView):
    """ Вывод списка подписчиков пользователя
    """
    permission_classes = [permissions.IsAuthenticated]
    # Используется сериализатор ListFollowerSerializer для конвертации данных модели Follower в формат JSON
    serializer_class = ListFollowerSerializer

    def get_queryset(self):
        # найти все записи, где наш юзер будет совпадать с юзером который на сайте
        # таким образом мы найдём всех подписчиков юзера
        return Follower.objects.filter(user=self.request.user)


class FollowerView(views.APIView):
    """ Добавление в подписчики
    """
    permission_classes = [permissions.IsAuthenticated]

    # http добавление нового подписчика
    def post(self, request, pk):
        try:
            user = User.objects.get(id=pk)
        except Follower.DoesNotExist:
            return response.Response(status=404)
        # Если пользователь существует, создается новый объект Follower с текущим аутентифицированным пользователем в
        # качестве подписчика и указанным id в качестве пользователя
        Follower.objects.create(subscriber=request.user, user=user)
        return response.Response(status=201)

    # http удаление подписки
    def delete(self, request, pk):
        try:
            sub = Follower.objects.get(subscriber=request.user, user_id=pk)
        except Follower.DoesNotExist:
            return response.Response(status=404)
        sub.delete()
        return response.Response(status=204)
