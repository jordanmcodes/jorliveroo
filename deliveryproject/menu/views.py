from django.shortcuts import render
from .models import FoodItem

def menu(request):
    items = FoodItem.objects.all()
    return render(request, 'menu/menu.html',{'items': items})

def burgers (request):
    items = FoodItem.objects.filter(category__name="Burgers")
    return render (request, 'menu/burgers.html', {'items': items} )

def pasta (request):
    items = FoodItem.objects.filter(category__name="Pasta")
    return render (request, 'menu/pasta.html', {'items': items})

def pizza (request):
    items = FoodItem.objects.filter(category__name="Pizza")
    return render (request, 'menu/pizza.html', {'items': items})

def fish (request):
    items = FoodItem.objects.filter(category__name="Fish")
    return render (request, 'menu/fish.html', {'items': items})

def soup (request):
    items = FoodItem.objects.filter(category__name="Soup")
    return render(request, 'menu/soup.html',{'items': items})

def sides (request):
    items = FoodItem.objects.filter(category__name="Sides")
    return render (request, 'menu/sides.html', {'items': items})

def curry (request):
    items = FoodItem.objects.filter(category__name="Curry")
    return render (request, 'menu/curry.html', {'items': items})

def vegan (request):
    items = FoodItem.objects.filter(category__name="Vegan")
    return render (request, 'menu/vegan.html', {'items': items})

def gluten_free (request):
    items = FoodItem.objects.filter(category__name="Gluten Free")
    return render (request, 'menu/gluten_free.html', {'items': items} )

def saver_menu (request):
    items = FoodItem.objects.filter(category__name="Saver Menu")
    return render (request, 'menu/saver_menu.html', {'items': items})   

def desserts (request):
    items = FoodItem.objects.filter(category__name="Desserts")
    return render (request, 'menu/desserts.html', {'items': items} )

def kids_menu (request):
    items = FoodItem.objects.filter(category__name="Kids Menu")
    return render (request, 'menu/kids_menu.html',{'items': items} )