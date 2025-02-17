from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import serializers, status, viewsets
from rest_framework.response import Response

from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
