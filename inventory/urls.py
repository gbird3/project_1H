from django.conf.urls import url

from . import views

app_name = 'inventory'
urlpatterns = [
    url(r'^index/$', views.view_inventory, name='index'),
    url(r'^delete/([0-9]+)/$', views.delete, name='delete_inventory'),
    url(r'^add/$', views.add, name='add'),
    url(r'^edit/([0-9]+)/$', views.editItem, name='editItem'),
    url(r'^notes/([0-9]+)/$', views.viewNotes, name='viewNotes'),
    url(r'^addNotes/([0-9]+)/$', views.addNotes, name='addNotes'),
]
