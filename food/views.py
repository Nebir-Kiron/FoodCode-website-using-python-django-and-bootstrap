from django.shortcuts import render
from django.http import HttpResponse
from . models import Item
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