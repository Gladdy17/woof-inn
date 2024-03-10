from django.db import models

# Create your models here.

class User(models.Model):
    User_number = models.PositiveIntegerField
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    description = models.TimeField()

def __str__(self):
    return f'User: {self.first_name} {self.last_name}'