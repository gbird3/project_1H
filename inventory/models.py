from django.db import models
from django.db import transaction
from django.contrib.auth.models import AbstractUser
from django.contrib import admin
import datetime


# Define models here
class Manufacturer(models.Model):
    '''A list of manufacturers for the items in inventory'''
    manufacturer = models.CharField(null=True, blank=True, max_length=100)
    def __str__(self):
       '''Prints for debugging purposes'''
       return 'Manufacturer: %s' % (self.manufacturer)

class Location(models.Model):
  '''A list of office locations'''
  location = models.CharField(null=True, blank=True, max_length=100)

  def __str__(self):
     '''Prints for debugging purposes'''
     return 'Location: %s' % (self.location)

class Item(models.Model):
    '''All of the items in the compay inventory'''
    name = models.CharField(null=True, blank=True, max_length=100)
    organizationalTag = models.CharField(null=True, blank=True, max_length=10)
    manufacturerPartNumber = models.CharField(null=True, blank=True, max_length=50)
    dateImplemented = models.DateField(null=True, blank=True, max_length=100)
    description = models.TextField(null=True, blank=True)
    location = models.ForeignKey(Location, related_name='locations')
    manufacturer = models.ForeignKey(Manufacturer, related_name='manufacturers')

    def __str__(self):
        '''Prints for debugging purposes'''
        return 'Item: %s' % (self.name)

class Note(models.Model):
    ''' Mainteance notes for specific inventory items'''
    note = models.TextField(null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    item = models.ForeignKey(Item, related_name='items')

    def __str__(self):
        '''Prints for debugging purposes'''
        return 'Note: %s' % (self.note)
