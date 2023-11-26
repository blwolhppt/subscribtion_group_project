import base64

from django.core.files.base import ContentFile
from rest_framework.fields import ImageField
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from subscribtions.models import Category

from users.models import User

from .constants import LENGTH, EMAIL_LENGTH
from users.validators import validate_username


# class CategorySerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Category
#        fields = '__all__'
#

class Base64ImageField(ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
        return super().to_internal_value(data)


class CustomUserCreateSerializer(UserCreateSerializer):
    username = serializers.CharField(
        max_length=LENGTH, required=True,
        validators=[validate_username,
                    UniqueValidator(queryset=User.objects.all())])

    email = serializers.EmailField(max_length=EMAIL_LENGTH, required=True,
                                   validators=[UniqueValidator])
    image = Base64ImageField(required=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'image',
                  'last_name', 'password')


class CustomUserSerializer(UserSerializer):
    image = Base64ImageField()

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'image',
                  'last_name')
