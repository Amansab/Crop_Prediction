from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager


# Create your models here.
class Register(models.Model):
    FirstName=models.CharField(max_length=30)
    LastName=models.CharField(max_length=30)
    Email=models.EmailField(max_length=30)
    password=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    dob=models.DateField(auto_now=False,null=True)

class Test(models.Model):
    n=models.FloatField(max_length=10)
    p=models.FloatField(max_length=10)
    k=models.FloatField(max_length=10)
    temp=models.FloatField(max_length=10)
    pH=models.FloatField(max_length=10)
    humidity=models.FloatField(max_length=10)
    rain=models.FloatField(max_length=10)
    


