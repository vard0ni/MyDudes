from django.contrib import admin

from profiles.models import Profile


# класс для описания того, как модель Profile должна быть отображена на административной странице
class ProfileAdmin(admin.ModelAdmin):
    # определение полей, которые можно редактировать прямо из списка в административной панели
    list_editable = ['first_name', 'last_name', 'verified']
    # определение, какие поля будут отображаться на странице списка моделей в административной панели.
    list_display = ['user_phone', 'user_email', 'first_name', 'last_name', 'verified']

    def user_phone(self, obj):
        return obj.user.phone

    def user_email(self, obj):
        return obj.user.email


admin.site.register(Profile, ProfileAdmin)
