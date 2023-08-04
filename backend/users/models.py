from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):

    # create_user создает нового пользователя с адресом электронной почты или номером телефона и паролем
    def create_user(self, email=None, phone=None, password=None):
        if not email and not phone:
            raise ValueError('Either email or phone must be set')
        user = self.model(
            email=self.normalize_email(email) if email else None,
            phone=phone,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # create_superuser делает то же самое, но также устанавливает пользовательские поля is_staff и is_superuser в True
    def create_superuser(self, email=None, phone=None, password=None):
        user = self.create_user(email=email, phone=phone, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# Мы также определяем пользовательскую модель User, которая расширяет класс Django AbstractBaseUser
# и использует наш собственный UserManager
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=True)
    phone = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=200)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.email or self.phone

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
