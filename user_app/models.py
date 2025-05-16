from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='users/', blank=True, null=True)
    description =  models.TextField(blank=True, null=True)
    date_to_register = models.DateField(auto_now_add=True)
    
    USERNAME_FIELD = 'email'   
    REQUIRED_FIELDS = ['username'] 