from django.db.models import Avg
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from inscriptions.models import Inscription
from inscriptions.serializers import InscriptionSerializer
from subjects.models import Subject

from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    @action(detail=True, methods=["get"])
    def subjects(self, request, pk=None):
        """
        Get the subjects of a student
        """
        student = self.get_object()
        inscriptions = Inscription.objects.filter(student=student)
        serializer = InscriptionSerializer(inscriptions, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def approved_subjects(self, request, pk=None):
        """
        Get the subjects of a student
        """
        student = self.get_object()
        approved_inscriptions = Inscription.objects.filter(
            student=student, is_approved=True
        )
        all_inscriptions = Inscription.objects.filter(student=student)
        serializer = InscriptionSerializer(approved_inscriptions, many=True)

        avg_score = (
            all_inscriptions.aggregate(Avg("calification"))["calification__avg"] or 0
        )

        response_data = {
            "approved_subjects": serializer.data,
            "avg_score": avg_score,
        }

        return Response(response_data)
