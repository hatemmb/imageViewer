from django.contrib import admin
from .models import Device, Image

# Register your models here.
# class DeviceAdmin(admin.ModelAdmin):
#     list_display = ('device_name', 'id')
    

admin.site.register(Device)
admin.site.register(Image)