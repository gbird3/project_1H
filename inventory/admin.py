from django.contrib import admin

from .models import Manufacturer, MaintenanceNote, Device

# Register your models here.
admin.site.register(Manufacturer)
admin.site.register(MaintenanceNote)
admin.site.register(Device)
