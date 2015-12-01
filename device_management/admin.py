from django.contrib import admin
from .models import Device, Log, MaintainLog



# Register your models here.

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'owner', 'info')


admin.site.register(Device, DeviceAdmin)
admin.site.register(Log)
admin.site.register(MaintainLog)

