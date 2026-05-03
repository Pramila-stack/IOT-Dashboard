from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_device_owner = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    