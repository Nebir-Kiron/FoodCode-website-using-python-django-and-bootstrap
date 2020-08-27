from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Item
from .forms import ItemForm
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
# Create your views here.
class Index(ListView):
    model = Item
    template_name='food/index.html'
    context_object_name='item_list'

def item(request):
    return HttpResponse("Item view")

class Details(DetailView):
    model=Item
    template_name = 'food/details.html'


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

def delete_item(request,id):
    item = Item.objects.get(id=id)
    if request.method == "POST":
        item.delete()
        return redirect('food:index')

    return render(request,'food/delete.html')