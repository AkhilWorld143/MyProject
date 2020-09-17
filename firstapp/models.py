from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50);
    username = models.CharField(max_length=50);
    gender = models.CharField(max_length=8);
    cities = models.CharField(max_length=20);
    image = models.ImageField(upload_to='stud_pics/');
    email = models.EmailField();
    password = models.CharField(max_length=20);
    status = models.IntegerField()
