# from django.urls import path
# from . import views

# urlpatterns = [
#     path('device', views.device_list, name='devices'),
#     path('create_device', views.device_create, name="createDevices")
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('device', views.DeviceList.as_view(), name='devices'),
    path('device/<str:device_name>', views.DeviceList.as_view(), name='devices'),
    path('images/<str:device_name>', views.ImageList.as_view(), name='images')
]
