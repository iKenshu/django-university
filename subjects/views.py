from django.shortcuts import render
from rest_framework import viewsets

from .models import Subject
from .serializers import SubjectSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows subjects to be viewed or edited.
    """

    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
