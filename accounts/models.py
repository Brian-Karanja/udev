from django.db import models

# Create your models here.
class login(models.Model):
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    course = models.CharField(max_length=50)
    schools = models.CharField(max_length=50)
