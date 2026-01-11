from django.db import models

# Create your models here.

class Purchase_info(models.Model):
    book_name = models.CharField(max_length=300)
    student_id = models.IntegerField()
    picup_time = models.DateField(blank=True, null=True)
    delivery_time = models.DateField(blank=True, null=True)