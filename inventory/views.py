from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Item
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required

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
        return HttpResponseRedirect('inventory/index/')

    item.delete()

    return HttpResponseRedirect('inventory/index/')
