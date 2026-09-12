from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    cpf = models.CharField(max_length=200,) 
    endereco = models.CharField(max_length=200)
