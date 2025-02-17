from django.db import models

from teachers.models import Teacher


class Subject(models.Model):
    """
    Subject model
    Atributes:
        name: name of the subject
        code: code of the subject
        teacher: teacher of the subject
        required_credits: required credits for the subject
        prerequisites: prerequisites of the subject
    """

    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    required_credits = models.IntegerField(default=0, blank=True, null=True)
    prerequisites = models.ManyToManyField("self", blank=True, symmetrical=False)

    def __str__(self):
        return self.name
