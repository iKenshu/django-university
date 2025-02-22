"""
URL configuration for djangouniversity project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.routers import DefaultRouter

from inscriptions.views import InscriptionViewSet
from students.views import StudentViewSet
from subjects.views import SubjectViewSet
from teachers.views import TeachersViewSet
from users.views import UserViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Django University",
        default_version="v1",
        description="Django University API",
    ),
    public=True,
)

router = DefaultRouter()
router.register("users", UserViewSet, basename="user")
router.register("teachers", TeachersViewSet, basename="teacher")
router.register("students", StudentViewSet, basename="student")
router.register("subjects", SubjectViewSet, basename="subject")
router.register("inscriptions", InscriptionViewSet, basename="inscription")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("users.urls")),
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]

urlpatterns += router.urls
