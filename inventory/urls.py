from django.conf.urls import url

from . import views

app_name = 'inventory'
urlpatterns = [
    url(r'^index/$', views.view_inventory, name='index'),
    url(r'^delete/([0-9]+)/$', views.delete, name='delete_inventory'),
    url(r'^add/$', views.add, name='add')
]
