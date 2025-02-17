from rest_framework import serializers

from .models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    """
    Serializer for the Teacher model
    """

    class Meta:
        model = Teacher
        fields = "__all__"
