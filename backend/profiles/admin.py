from django.contrib import admin

from profiles.models import Profile


class ProfileAdmin(admin.ModelAdmin):

    list_display = ['user_phone', 'user_email', 'first_name', 'last_name']

    def user_phone(self, obj):
        return obj.user.phone

    def user_email(self, obj):
        return obj.user.email


admin.site.register(Profile, ProfileAdmin)
