from django.db import models
from django.db import transaction
from django.contrib.auth.models import AbstractUser
from django.contrib import admin
import datetime


#####################################################################
###   User class


# Define models here
class Manufacturer(models.Model):
    '''An image for a product'''
    manufacturer = models.TextField(null=True, blank=True)
    def __str__(self):
       '''Prints for debugging purposes'''
       return 'Manufacturer: %s' % (self.manufacturer)

class Location(models.Model):
  '''An image for a product'''
  location = models.TextField(null=True, blank=True)

  def __str__(self):
     '''Prints for debugging purposes'''
     return 'Location: %s' % (self.location)

class Item(models.Model):
  name = models.TextField(null=True, blank=True)
  description = models.TextField(null=True, blank=True)
  location = models.ForeignKey(Location, related_name='locations')
  manufacturer = models.ForeignKey(Manufacturer, related_name='manufacturers')

  def __str__(self):
    '''Prints for debugging purposes'''
    return 'Item: %s' % (self.name)

class Note(models.Model):
  note = models.TextField(null=True, blank=True)
  date = models.DateTimeField(null=True, blank=True)
  item = models.ForeignKey(Item, related_name='items')

  def __str__(self):
    '''Prints for debugging purposes'''
    return 'Note: %s' % (self.note)
