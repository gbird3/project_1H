from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    '''A list of all manufacturers of devices'''
    name = models.CharField(max_length=100, null=True, blank=True)

class Device(models.Model):
    '''A list of all the devices that the company has'''
    location = models.CharField(max_length=100, null=True, blank=True)
    organizationalTag = models.CharField(max_length=100, null=True, blank=True)
    manufacturerId = models.ForeignKey(Manufacturer, related_name="manufacturers")
    manPartNumber = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=0)
    description = models.TextField(null=True, blank=True)
    dateImplemented = models.DateField(null=True, blank=True)

class MaintenanceNote(models.Model):
    '''A list of all maintenance notes for a device'''
    deviceId = models.ForeignKey(Device, related_name="devices")
    note = models.TextField(null=True, blank=True)
