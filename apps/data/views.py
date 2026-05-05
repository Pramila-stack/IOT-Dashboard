from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import SensorDataSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.devices.models import Device
from .models import SensorData

class SensorDataCreateAPIView(APIView):

    def post(self, request):
        serializer = SensorDataSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Data saved successfully"},
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



class DeviceDataListAPIView(APIView):

    def get(self, request, device_id):
        try:
            device = Device.objects.get(id=device_id)
        except Device.DoesNotExist:
            return Response({"error": "Device not found"}, status=404)

        data = SensorData.objects.filter(device=device).order_by('-created_at')

        results = [
            {
                "temperature": d.temperature,
                "humidity": d.humidity,
                "energy": d.energy,
                "timestamp": d.created_at
            }
            for d in data
        ]

        return Response({
            "device": device.name,
            "count": len(results),
            "data": results
        })
    
class LatestDeviceDataAPIView(APIView):

    def get(self, request, device_id):
        try:
            device = Device.objects.get(id=device_id)
        except Device.DoesNotExist:
            return Response({"error": "Device not found"}, status=404)

        latest = SensorData.objects.filter(device=device).order_by('-created_at').first()

        if not latest:
            return Response({"message": "No data found"})

        return Response({
            "device": device.name,
            "temperature": latest.temperature,
            "humidity": latest.humidity,
            "energy": latest.energy,
            "timestamp": latest.created_at
        })