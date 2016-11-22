from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Item, Location, Manufacturer
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from django import forms

# Create your views here.
@login_required(login_url='/account/login/')
def view_inventory(request):
	'''Lists the inventory in a table on the screen'''

	items = Item.objects.all().order_by('name')

	template_vars = {
		'items': items,
	}
	return render(request, 'inventory/index.html', template_vars)

@login_required(login_url='/account/login/')
def delete(request, id):
    '''Deletes an inventory item'''

    try:
        item = Item.objects.get(id = id)
    except Item.DoesNotExist:
        return HttpResponseRedirect('/inventory/index/')

    item.delete()

    return HttpResponseRedirect('/inventory/index/')

@login_required(login_url='/account/login/')
def add(request):
	'''Adds an item to the inventory'''

	form = AddItemForm()
	if request.method == 'POST':
		form = AddItemForm(request.POST)
		if form.is_valid():
			i = Item()
			i.name = form.cleaned_data.get('name')
			i.organizationalTag = form.cleaned_data.get('organizationalTag')
			i.manufacturerPartNumber = form.cleaned_data.get('manufacturerPartNumber')
			i.dateImplemented = form.cleaned_data.get('dateImplemented')
			i.description = form.cleaned_data.get('description')
			i.location = form.cleaned_data.get('location')
			i.manufacturer = form.cleaned_data.get('manufacturer')

			i.save()

			return HttpResponseRedirect('/inventory/index')


	template_vars = {
		'form': form
	}

	return render(request, 'inventory/add.html', template_vars)
class AddItemForm(forms.Form):
	name = forms.CharField(label='Name', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	organizationalTag = forms.CharField(label='Organizational Tag', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	manufacturerPartNumber = forms.CharField(label='Manufacturer Part Number', required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	dateImplemented = forms.DateField(label='Date Implemented', widget=forms.TextInput(attrs={'class': 'form-control'}))
	description = forms.CharField(label='Description', required=True, max_length=140, widget=forms.Textarea(attrs={'class': 'form-control'}))
	location = forms.ModelChoiceField(label='Location', required=True, queryset=Location.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
	manufacturer = forms.ModelChoiceField(label='Manufacturer', required=True, queryset=Manufacturer.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
