from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from wall.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """ Посты
    """
    list_display = ("user", "published", "date", "moderation", "views", "id")


@admin.register(Comment)
class CommentAdmin(MPTTModelAdmin, admin.ModelAdmin):
    """ Коментарии к постам
    """
    list_display = ("user", "post", "created_date", "update_date", "published", "id")
    # actions = ['unpublish', 'publish']
    mptt_level_indent = 15
