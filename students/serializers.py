"""
This file contains the serializers for the students app
"""

from rest_framework import serializers

from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Student model
    """

    class Meta:
        model = Student
        fields = "__all__"
