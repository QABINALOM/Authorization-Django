from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms


class User(AbstractUser):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=100, unique = True)
    password = models.CharField(max_length=200)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username'] 