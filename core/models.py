from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email=models.EmailField(unique=True)
    username=models.CharField(max_length=200)
    subject=models.CharField(max_length=200)
    message = models.CharField(max_length=255)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']
    def __str__(self):
        return self.username

# Create your models here.
class Customer(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=200)
    telephone = models.CharField(max_length=15)  # Assuming a maximum length of 15 for phone numbers
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.username
