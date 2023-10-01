from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin  # класс добавляет поля необходимые для обработки уровней доступа
from django.db import models
# сигнал, отправляемый после сохранения экземпляра модели.
from django.db.models.signals import post_save

from profiles.models import Profile


class UserManager(BaseUserManager):
    # менеджер должен использоваться Django при создании миграций базы данных
    use_in_migrations = True

    # create_user создает нового пользователя с адресом электронной почты или номером телефона и паролем
    def create_user(self, email, phone, password=None):
        if not email and not phone:
            raise ValueError('Either email or phone must be set')
        user = self.model(
            email=self.normalize_email(email) if email else None,
            phone=phone,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # create_superuser делает то же самое, но также устанавливает права суперпользователя
    def create_superuser(self, email=None, phone=None, password=None):
        user = self.create_user(email=email, phone=phone, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# Мы также определяем пользовательскую модель User, которая расширяет класс Django AbstractBaseUser
# и использует наш собственный UserManager
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True, null=True)
    phone = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=200)

    # Атрибуты, определяющие активность пользователя, его принадлежность к персоналу и статус суперпользователя.
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Указывается поле, которое будет использоваться в качестве имени пользователя
    USERNAME_FIELD = 'phone'
    # поля, которые должны быть заполнены при создании пользователя
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    # строковое представление объекта
    def __str__(self):
        return self.email or self.phone

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    # Метод для получения профиля данного пользователя
    def profile(self):
        profile = Profile.objects.get(user=self)


# Функция для создания профиля при создании пользователя.
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# Функция, обеспечивающая сохранение профиля при сохранении пользователя
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# Подключение функций create_user_profile и save_user_profile к сигналу post_save для модели User, так что каждый раз,
# когда происходит сохранение экземпляра User, эти функции вызываются автоматически.
post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
