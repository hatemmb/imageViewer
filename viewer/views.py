# from django.shortcuts import render
# from .models import Device
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .serializer import DeviceSerializer
# from viewer import serializer

# # Create your views here.


# @api_view(['GET'])
# def device_list(request):
#     devices = Device.objects.all()
#     serializer = DeviceSerializer(devices, many=True)

#     return Response(serializer.data)

# @api_view(['POST'])
# def device_create(request):
#     serializer = DeviceSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors)

from .models import Device, Image
from .serializer import DeviceSerializer, ImageSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime


class DeviceList(APIView):
    def get(self, request, device_name):
        device = Device.objects.get(device_name = device_name)
        # devices = Device.objects.all()
        serializer = DeviceSerializer(device)
        return Response(serializer.data)

    def post(self, request):
        data = {}
        try:
            last_object_id = Device.objects.last().id
        except:
            last_object_id = 0
        data['device_name'] = 'Device' + str(last_object_id + 1)
        data['dynamic_device_name'] = 'Device' + str(last_object_id + 1)
        data['edited'] = False
        serializer = DeviceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImageList(APIView):
    def get(self, request ,device_name):
        device_id = Device.objects.get(device_name=device_name).id
        device = Device.objects.get(device_name = device_name)
        device.edited = False
        device.save()
        images = Image.objects.filter(device=device_id)
        f_images = images.filter(end_time__gte=datetime.now().astimezone())
        serializer = ImageSerializer(f_images, many=True)
        return Response(serializer.data)