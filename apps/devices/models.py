import uuid

from django.db import models

from config import settings

# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    api_key = models.UUIDField(default=uuid.uuid4,unique=True,editable=False)

    device_type = models.CharField(max_length=50,default='sensor')
    location = models.CharField(max_length=100,blank=True,null=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

    