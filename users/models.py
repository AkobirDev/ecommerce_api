from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    photo = models.ImageField(default='anonimous.png', blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ('-date_joined',)

