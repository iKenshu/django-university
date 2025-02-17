from django.db import models


class Teacher(models.Model):
    """
    Teacher model
    Atributes:
        name: name of the teacher
        email: email of the teacher
        specialty: specialty of the teacher
    """

    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    specialty = models.CharField(max_length=200)

    def __str__(self):
        return self.name
