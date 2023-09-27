from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Profile(models.Model):
    # Profile of user

    GENDER = (
        ('male', 'male'),
        ('female', 'female')
    )

    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER, default='male')
    hobbies = models.ManyToManyField('Hobby', related_name='users', blank=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.phone


class Hobby(models.Model):
    # Hobbies model
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
