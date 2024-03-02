from django.db import models

# Create your models here.
class Employee(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    dept = models.CharField(max_length=30)
    salary = models.IntegerField()
    mobile = models.IntegerField()
    add = models.CharField(max_length=30)