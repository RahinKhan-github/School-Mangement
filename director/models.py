from django.db import models
# from authentication.models import CustomUser

# Create your models here.
class role (models.Model):
    name=models.CharField(max_length=100)