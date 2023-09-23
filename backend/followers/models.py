from django.conf import settings
from django.db import models


class Follower(models.Model):
    """ Модель подписчиков
    """

    # пользователь на которого мы подписываемся
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owner'
    )

    # подписчики пользователя
    subscriber = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='subscribers'
    )
