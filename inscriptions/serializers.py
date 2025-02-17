"""
This file contains the serializers for the inscriptions app
"""

from rest_framework import serializers
from rest_framework.response import Response

from students.models import Student
from subjects.models import Subject

from .models import Inscription


class InscriptionSerializer(serializers.ModelSerializer):
    """
    Serializer for the Inscription model
    """

    student_name = serializers.ReadOnlyField(source="student.name")
    subject_name = serializers.ReadOnlyField(source="subject.name")

    class Meta:
        model = Inscription
        fields = "__all__"


class BulkInscriptionSerializer(serializers.Serializer):
    """
    Serializer for bulk inscriptions with multiple subjects
    """

    student_id = serializers.IntegerField()
    inscriptions = serializers.ListField(child=serializers.DictField())

    def create(self, validated_data):
        """
        Create multiple inscriptions
        """
        student = Student.objects.get(id=validated_data.get("student_id"))
        inscriptions_data = validated_data.get("inscriptions")
        inscriptions = []

        for ins_data in inscriptions_data:
            subject = Subject.objects.get(id=ins_data["subject_id"])
            calification = ins_data.get("calification", 0)
            is_approved = calification >= 3.0

            inscriptions.append(
                Inscription(
                    subject=subject,
                    student=student,
                    calification=calification,
                    is_approved=is_approved,
                )
            )

        return Inscription.objects.bulk_create(inscriptions)
