from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from apps.comman.models import User
from apps.comman.serializers import UserSerializer

class UserViewSet(CreateModelMixin,GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer