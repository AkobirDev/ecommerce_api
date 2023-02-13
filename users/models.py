from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    photo = models.ImageField(default='anonimous.png')
    phone_number = models.IntegerField()
    address = models.CharField(max_length=300)

    class Meta:
        ordering = ('-date_joined',)
