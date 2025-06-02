from django.db import models

from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth import get_user_model
# # Create your models here.

class User(AbstractUser):
    USER_TYPES = (
        ('admin', 'Admin'),
        ('freelancer', 'Freelancer'),
        ('client', 'Client'),
    )

    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    bio= models.TextField(blank= True)
    pass


User =get_user_model()

class Visitor(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    session_key = models.CharField(max_length=40, blank=True, null= True)
    ip_address = models.CharField(max_length=45)
    user_agent = models.TextField(null=True, blank=True)
    path = models.CharField(max_length=255)
    method = models.CharField(max_length=10)
    duration = models.FloatField()  # in seconds
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['ip_address']),
            models.Index(fields=['user']),
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return f"{self.ip_address} - {self.path} ({self.duration:.2f}s)"
    

