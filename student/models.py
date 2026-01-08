from django.db import models

# Create your models here.
class Student_account(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.IntegerField(unique=True)
    session = models.CharField(max_length=40)

    def __str__(self):
        return str(self.student_id)