from django.contrib import admin

from apps.devices.models import Device

# Register your models here.
from django.contrib import admin
from .models import Device

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'device_type', 'api_key', 'is_active', 'created_at')
    readonly_fields = ('api_key',)

admin.site.register(Device, DeviceAdmin)