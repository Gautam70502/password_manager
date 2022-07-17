import email
from email.mime import application
from unicodedata import name
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Password_Manager(models.Model):

    #user = models.ForeignKey(User,on_delete=models.CASCADE)
    Email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    application_name = models.CharField(max_length=50)
    logo = models.CharField(max_length=300)
    
    

    class Meta:
        ordering = ["-id"]
    

