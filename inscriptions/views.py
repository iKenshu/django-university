from django.shortcuts import render
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
