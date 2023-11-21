from django.contrib.auth.models import AbstractUser
from django.db import models

from .constants import EMAIL_LENGTH, LENGTH
from .validators import validate_username


class User(AbstractUser):
    email = models.EmailField(max_length=EMAIL_LENGTH,
                              unique=True,
                              blank=False,
                              null=False,
                              verbose_name="Почта")

    username = models.CharField(validators=(validate_username,),
                                max_length=LENGTH,
                                unique=True,
                                blank=False,
                                null=False,
                                verbose_name='Никнейм')

    image = models.ImageField(verbose_name='Картинка профиля',
                              upload_to='users/')

    first_name = models.CharField(max_length=LENGTH,
                                  blank=False,
                                  null=False,
                                  verbose_name="Имя")

    last_name = models.CharField(max_length=LENGTH,
                                 blank=False,
                                 null=False,
                                 verbose_name="Фамилия")

    password = models.CharField(max_length=LENGTH,
                                verbose_name="Пароль")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', 'first_name', 'last_name')

    def __str__(self):
        return self.username
