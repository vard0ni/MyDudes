from django.db import models
from django.conf import settings
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from comments.models import AbstractComment


class Post(models.Model):
    """ Post model
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    text = models.CharField(max_length=500, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)
    moderation = models.BooleanField(default=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        # Post by {self.user} -
        return f'id {self.id}'

    def comments_count(self):
        return self.comments.count()


class Comment(AbstractComment, MPTTModel):
    """ Модель коментариев к постам
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    parent = TreeForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children'
    )

    def __str__(self):
        return "{} - {}".format(self.user, self.post)
