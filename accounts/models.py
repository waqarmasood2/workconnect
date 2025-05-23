from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    USER_TYPES = (
        ('admin', 'Admin'),
        ('freelancer', 'Freelancer'),
        ('client', 'Client'),
    )

    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    bio= models.TextField(blank= True)
