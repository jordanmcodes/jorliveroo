from django.shortcuts import render
from .models import FoodItem

def menu(request):
    items = FoodItem.objects.all()
    return render(request, 'menu/menu.html',{'items': items})

