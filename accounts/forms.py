from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegistrationFrom(UserCreationForm):
    class meta:
        model =User
        fields =['']