from django.db import models

# Create your models here.
class Student(models.Model):
    std_id = models.CharField(max_length=100)
    std_name = models.CharField(max_length=200)
    std_email = models.EmailField(max_length=100)
    std_number = models.CharField(max_length=120)
    class Meta:
        db_table = "student"