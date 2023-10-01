from rest_framework import serializers
from profiles.serializers import UserByFollowerSerializer
from .models import Follower


#  класс для преобразования инстансов модели Follower в JSON.
class ListFollowerSerializer(serializers.ModelSerializer):
    #  many - указываем, что может быть несколько подписчиков для одной модели Follower и все они будут сериализованы
    # read_only=True говорит об том, что данное поле только на чтение и не может быть изменено через API.
    subscribers = UserByFollowerSerializer(many=True, read_only=True)

    # конфигурация для ListFollowerSerializer
    class Meta:
        # модель для сериализации
        model = Follower
        #  поля, которые следует включить в сериализированный вывод
        fields = ('subscribers',)
