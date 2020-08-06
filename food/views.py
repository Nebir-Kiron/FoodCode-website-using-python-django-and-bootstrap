from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Item
from .forms import ItemForm
# Create your views here.
def index(request):
    item_list = Item.objects.all()
    contex = {
        'item_list':item_list,
    }
    return render(request,'food/index.html',contex)

def item(request):
    return HttpResponse("Item view")

def details(request,id):
    item = Item.objects.get(id=id)
    contex = {
        'item':item,
    }
    return render(request,'food/details.html',contex)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    contex = {
        'form':form,
    }

    return render(request,'food/additem.html',contex)

def update_item(request,id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None,instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    contex = {
        'form':form,
    }

    return render(request,'food/update.html',contex)