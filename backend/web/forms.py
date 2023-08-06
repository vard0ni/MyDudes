from django.contrib.auth.forms import UserCreationForm

from users.models import User


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Met):
        model = User
        fields = UserCreationForm.Meta.fields + ("email",)
