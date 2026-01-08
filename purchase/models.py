from django.db import models

# Create your models here.

class Purchase_info(models.Model):
    names = models.CharField(max_length=300)
    student_id = models.IntegerField()
    when_purchased = models.DateTimeField(auto_now_add=True)
    delivery_time = models.DateTimeField()