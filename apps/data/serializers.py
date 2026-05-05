from rest_framework import serializers
from .models import SensorData
from apps.devices.models import Device

class SensorDataSerializer(serializers.ModelSerializer):
    api_key = serializers.UUIDField(write_only=True)

    class Meta:
        model = SensorData
        fields = ['api_key', 'temperature', 'humidity', 'energy', 'created_at']
        read_only_fields = ['created_at']

    def create(self, validated_data):
        api_key = validated_data.pop('api_key')

        try:
            device = Device.objects.get(api_key=api_key, is_active=True)
        except Device.DoesNotExist:
            raise serializers.ValidationError("Invalid API Key")

        return SensorData.objects.create(device=device, **validated_data)