from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Item, Location, Manufacturer, Note
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from django import forms
from datetime import datetime

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
	organizationalTag = forms.CharField(label='Organizational Tag', required=True, max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
	manufacturerPartNumber = forms.CharField(label='Manufacturer Part Number', required=True, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
	dateImplemented = forms.DateField(label='Date Implemented', widget=forms.TextInput(attrs={'class': 'form-control'}))
	description = forms.CharField(label='Description', required=True, max_length=140, widget=forms.Textarea(attrs={'class': 'form-control'}))
	location = forms.ModelChoiceField(label='Location', required=True, queryset=Location.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
	manufacturer = forms.ModelChoiceField(label='Manufacturer', required=True, queryset=Manufacturer.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

@login_required(login_url='/account/login/')
def editItem(request, itemId):
	''' Edits an item'''
	try:
		item = Item.objects.get(id = itemId)
	except Item.DoesNotExist:
		return HttpResponseRedirect('/inventory/index/')

	form = AddItemForm(initial={'name': item.name, 'organizationalTag': item.organizationalTag, 'manufacturerPartNumber': item.manufacturerPartNumber, 'dateImplemented': item.dateImplemented, 'description': item.description, 'location': item.location, 'manufacturer': item.manufacturer})

	if request.method == 'POST':
		form = AddItemForm(request.POST)
		if form.is_valid():
			i = Item.objects.get(id = itemId)
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
		'form': form,
		'item': item
	}

	return render(request, 'inventory/editItem.html', template_vars)

@login_required(login_url='/account/login/')
def viewNotes(request, itemId):
	''' Shows a list of all the notes for a specific item '''
	notes = Note.objects.all().filter(item = itemId)
	item = Item.objects.get(id = itemId)

	template_vars = {
		'notes': notes,
		'item': item
	}
	return render(request, 'inventory/notes.html', template_vars)

@login_required(login_url='/account/login/')
def addNotes(request, itemId):
	'''Allows for adding a maintenance note to a specific item '''
	form = NoteForm()
	item = Item.objects.get(id = itemId)

	if request.method == 'POST':
		form = NoteForm(request.POST)
		if form.is_valid():

			n = Note()
			n.note = form.cleaned_data.get('note')
			n.date = datetime.now()
			n.item = item
			n.save()

			return HttpResponseRedirect('/inventory/index')

	template_vars = {
		'form': form,
		'item': item
	}

	return render(request, 'inventory/addNotes.html', template_vars)

class NoteForm(forms.Form):
	note = forms.CharField(label='Note', required=True, max_length=300, widget=forms.Textarea(attrs={'class': 'form-control'}))
	# item = forms.ModelChoiceField(label='Item', required=True, queryset=Item.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
