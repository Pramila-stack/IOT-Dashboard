from django.db import models

from apps.devices.models import Device

# Create your models here.


class DeviceSummary(models.Model):
    device = models.OneToOneField(Device,on_delete=models.CASCADE)

    avg_temperature = models.FloatField(default=0)
    total_energy = models.FloatField(default=0)
    last_updated = models.DateTimeField(auto_now_add=True)
    