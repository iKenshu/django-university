from django.db import models


class Student(models.Model):
    """
    Student model
    Atributes:
        name: name of the student
        email: email of the student
        dni: dni of the student
        birth_date: birth date of the student
    """

    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    dni = models.CharField(max_length=200)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name
