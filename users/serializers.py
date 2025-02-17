"""
This file contains the serializers for the users app
"""

from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """
    This is a serializer for the User model
    """

    class Meta:
        model = User
        fields = ("id", "username", "email")
