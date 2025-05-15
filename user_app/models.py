from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    image = models.ImageField(upload_to='users/', blank=True, null=True)
    description =  models.TextField(blank=True, null=True)
    dateToRegister = models.DateField(auto_now_add=True)