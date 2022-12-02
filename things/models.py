from django.contrib.auth.models import AbstractUser
from django.db import models

class Thing(AbstractUser):
    name = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=200, blank=True)
    quantity = models.IntegerField(default=0, blank=False)