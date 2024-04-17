from django.db import models

# Create your models here.
from django.db import models
from director.models import role
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from .manager import CustomUserManager

class CustomUser(AbstractUser ,PermissionsMixin):
    first_name = models.CharField(max_length=100, null=False)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, null=False)
    password=models.CharField(max_length=100, null=False)
    email = models.EmailField(unique=True, null=False)

    role = models.ManyToManyField(role, blank=True, on_delete=models.SET_NULL)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']