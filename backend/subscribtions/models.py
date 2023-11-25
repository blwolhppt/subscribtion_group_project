from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator

from .constants import LENGTH, LENGTH_SLUG
from users.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=LENGTH,
                            verbose_name='Название категории', unique=True)
    slug = models.SlugField(max_length=LENGTH_SLUG,
                            verbose_name='Cлаг', unique=True)

    class Meta:
        verbose_name = 'Категория'

    def __str__(self):
        return self.name


class Subscription(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name='Автор подписки')
    name = models.CharField(max_length=LENGTH,
                            verbose_name='Название')
    category = models.ManyToManyField(Category, verbose_name='Категории')
    price = models.IntegerField(default=1, verbose_name='Цена')
    data = models.IntegerField(validators=[MinValueValidator(1),
                                           MaxValueValidator(31)],
                               verbose_name='Дата подписки')
    pub_date = models.DateTimeField(verbose_name='Дата', auto_now_add=True)

    class Meta:
        verbose_name = 'Подписки'
        ordering = ['-pub_date']

    def __str__(self):
        return self.name
