"""
This file contains the tests for the inscriptions app
"""

from django.test import TestCase
from rest_framework import status

from .models import Inscription
from .serializers import InscriptionSerializer


class InscriptionTestCase(TestCase):
    """
    This class contains the tests for the inscriptions app
    """

    def setUp(self):
        """
        Set up the test
        """
        self.data = {
            "subject": 1,
            "student": 1,
            "calification": 5,
            "is_approved": True,
        }

        self.inscription = Inscription.objects.create(**self.data)
        self.url = "/inscriptions/"

    def test_create_inscription(self):
        """
        Test the creation of an inscription
        """
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Inscription.objects.count(), 1)

    def test_get_inscriptions(self):
        """
        Test the get inscriptions
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Inscription.objects.count(), 1)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["subject"], self.data["subject"])
        self.assertEqual(response.data[0]["student"], self.data["student"])
        self.assertEqual(response.data[0]["calification"], self.data["calification"])
        self.assertEqual(response.data[0]["is_approved"], self.data["is_approved"])
