from django.shortcuts import render
from .models import FoodItem

def menu(request):
    items = FoodItem.objects.all()
    return render(request, 'menu/menu.html',{'items': items})

def burgers (request):
    return render (request, 'menu/burgers.html')

def pasta (request):
    return render (request, 'menu/pasta.html')

def pizza (request):
    return render (request, 'menu/pizza.html')

def fish (request):
    return render (request, 'menu/fish.html')

def soup (request):
    return render (request, 'menu/soup.html')

def sides (request):
    return render (request, 'menu/sides.html')

def curry (request):
    return render (request, 'menu/curry.html')

def vegan (request):
    return render (request, 'menu/vegan.html')

def gluten_free (request):
    return render (request, 'menu/gluten_free.html')

def saver_menu (request):
    return render (request, 'menu/saver_menu.html')    

def desserts (request):
    return render (request, 'menu/desserts.html')

def kids_menu (request):
    return render (request, 'menu/kids_menu.html')