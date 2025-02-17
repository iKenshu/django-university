from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from inscriptions.models import Inscription
from inscriptions.serializers import InscriptionSerializer
from students.models import Student
from students.serializers import StudentSerializer
from subjects.models import Subject
from subjects.serializers import SubjectSerializer

from .models import Teacher
from .serializers import TeacherSerializer


class TeachersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    @action(detail=True, methods=["get"])
    def subjects(self, request, pk=None):
        """
        Get the subjects of a teacher
        """
        teacher = self.get_object()
        subjects = Subject.objects.filter(teacher=teacher)
        serializer = SubjectSerializer(subjects, many=True)
        return Response(
            {"teacher": TeacherSerializer(teacher).data, "subjects": serializer.data}
        )

    @action(detail=True, methods=["get"])
    def students(self, request, pk=None):
        """
        Get the students of a teacher
        """
        teacher = self.get_object()
        subjects = Subject.objects.filter(teacher=teacher)
        inscriptions = Inscription.objects.filter(subject__in=subjects)
        students = {inscription.student for inscription in inscriptions}
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    @action(
        detail=True,
        methods=["get"],
        url_path="subjects/(?P<subject_id>[^/.]+)/students",
    )
    def students_subjects(self, request, pk=None, subject_id=None):
        """
        Get the students of a subject
        """
        teacher = self.get_object()
        subject = Subject.objects.get(id=subject_id, teacher=teacher)
        inscriptions = Inscription.objects.filter(subject=subject)
        students = {inscription.student for inscription in inscriptions}
        serializer = StudentSerializer(students, many=True)
        return Response(
            {
                "teacher": TeacherSerializer(teacher).data,
                "subject": SubjectSerializer(subject).data,
                "students": serializer.data,
            }
        )

    @action(
        detail=True, methods=["get"], url_path="subjects/(?P<subject_id>[^/.]+)/grades"
    )
    def subject_grades(self, request, pk=None, subject_id=None):
        """
        Get the grades of a subject
        """
        teacher = self.get_object()
        subject = Subject.objects.get(id=subject_id, teacher=teacher)
        inscriptions = Inscription.objects.filter(subject=subject)
        serializer = InscriptionSerializer(inscriptions, many=True)
        return Response(
            {
                "teacher": TeacherSerializer(teacher).data,
                "subject": SubjectSerializer(subject).data,
                "grades": serializer.data,
            }
        )
