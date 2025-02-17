"""
This file contains the urls for the teachers app
"""

from django.urls import path

from .views import TeacherViewSet

urlpatterns = [
    path("", TeacherViewSet.as_view()),
]
