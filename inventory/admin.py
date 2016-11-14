from django.contrib import admin

from .models import Item, Note, Location, Manufacturer

# Register your models here.
admin.site.register(Item)
admin.site.register(Note)
admin.site.register(Location)
admin.site.register(Manufacturer)
