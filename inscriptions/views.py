"""
This file contains the views for the inscriptions app
"""

from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Inscription
from .serializers import BulkInscriptionSerializer, InscriptionSerializer


class InscriptionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows inscriptions to be viewed or edited.
    """

    queryset = Inscription.objects.all()
    serializer_class = InscriptionSerializer

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "student_id": openapi.Schema(type=openapi.TYPE_INTEGER),
                "inscriptions": openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            "subject_id": openapi.Schema(type=openapi.TYPE_INTEGER),
                            "calification": openapi.Schema(type=openapi.TYPE_NUMBER),
                        },
                    ),
                ),
            },
        )
    )
    def create(self, request, *args, **kwargs):
        """
        Create multiple inscriptions
        """

        serializer = BulkInscriptionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {"message": "Inscriptions created successfully"},
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
