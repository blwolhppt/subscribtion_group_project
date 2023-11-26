from django.shortcuts import render
from djoser.views import UserViewSet

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from users.models import User

from api import serializers

from subscribtions.models import Category


# Create your views here.

class CustomUserViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.CustomUserSerializer
    pagination_class = LimitOffsetPagination

    http_method_names = ['get', 'post', 'delete', 'patch']

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return super().get_permissions()

    @action(
        detail=False,
        methods=('GET',),
        permission_classes=(IsAuthenticated,))
    def me(self, request):
        serializer = serializers.CustomUserSerializer(
            request.user, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    pagination_class = None
