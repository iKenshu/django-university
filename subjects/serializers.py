"""
This file contains the serializers for the subjects app
"""

from rest_framework import serializers

from .models import Subject


class SubjectSerializer(serializers.ModelSerializer):
    """
    Serializer for the Subject model
    """

    class Meta:
        model = Subject
        fields = "__all__"
