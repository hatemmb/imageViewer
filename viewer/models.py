from email.policy import default
from enum import unique
from unittest.util import _MAX_LENGTH
from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.




class Device(models.Model):

    device_name = models.CharField(max_length=30, unique=True, editable=False)
    dynamic_device_name = models.CharField(max_length=30, unique=True)
    #end_time = models.DateTimeField(null=True, blank=True)
    edited = models.BooleanField(null=True, blank=True, editable=False)
    def setEdited(device_name):
        device = Device.objects.get(dynamic_device_name = device_name)
        device.edited = True
        device.save()
    
    def __str__(self):
        return self.dynamic_device_name





class Image(models.Model):
    
    # def get_upload_path(instance):
    #     return '{0}/images'.format(Device.objects.get())
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    time = models.IntegerField(default=5, validators=[MinValueValidator(5), MaxValueValidator(60)])
    end_time = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        Device.setEdited(self.device)
        super(Image, self).save(*args, **kwargs)

    def delete(self):
        Device.setEdited(self.device)
        super(Image, self).delete()
    
    def __str__(self):
        return self.device.dynamic_device_name



