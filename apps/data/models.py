from django.db import models

from apps.devices.models import Device

# Create your models here.

class SensorData(models.Model):
    device = models.ForeignKey(Device,on_delete=models.CASCADE)
    temperature = models.FloatField(null=True,blank=True)
    humidity = models.FloatField(null=True,blank=True)
    energy = models.FloatField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
        