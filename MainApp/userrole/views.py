from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .Models.user import User
from .serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
