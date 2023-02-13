from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUse(AbstractUser):
    photo = models.ImageField(default='media/anonimous.png', blank=True)
    
