from django.urls import path
from .views import DeviceDataListAPIView, LatestDeviceDataAPIView, SensorDataCreateAPIView

urlpatterns = [
    path('sensor-data/', SensorDataCreateAPIView.as_view(), name='sensor-data'),
    # GET APIs
    path('device/<int:device_id>/data/', DeviceDataListAPIView.as_view()),
    path('device/<int:device_id>/latest/', LatestDeviceDataAPIView.as_view()),
]