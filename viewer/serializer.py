from tokenize import blank_re
from rest_framework import serializers
from .models import Device, Image
# from django.core.files import File
import base64


class DeviceSerializer(serializers.Serializer):
    device_name = serializers.CharField(max_length=30)
    dynamic_device_name = serializers.CharField(max_length=30)
    edited = serializers.BooleanField()

    def create(self, data):
        return Device.objects.create(**data)

class ImageSerializer(serializers.Serializer):
    base64_image = serializers.SerializerMethodField()
    time =  serializers.IntegerField()
    end_time = serializers.DateTimeField()
    def get_base64_image(self, obj):
        f = open(obj.image.path, 'rb')
        data = base64.b64encode(f.read())
        f.close()
        return data


# def decoding(encoded_data):
#     import base64
#     decoded_data = base64.b64decode((encoded_data))
#     #img_file = open('image' + i + '.jpeg', 'wb')
#     img_file = open('image.jpeg', 'wb')
#     img_file.write(decoded_data)
#     img_file.close()

