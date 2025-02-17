from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from students.models import Student
from subjects.models import Subject


class Inscription(models.Model):
    """
    Inscriptions model
    Atributes:
        subject: subject of the inscription
        student: student of the inscription
        calification: calification of the inscription
        is_approved: is approved of the inscription
        created_date: created date of the inscription
    """

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    calification = models.IntegerField(
        default=0,
        blank=True,
        null=True,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
    )
    is_approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} - {self.student}"

    def save(self, *args, **kwargs):
        """
        Save the inscription
        """
        if self.calification:
            self.is_approved = self.calification >= 3
        super().save(*args, **kwargs)
