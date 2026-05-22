from django.shortcuts import render
from .models import FoodItem

def menu(request):
    items = FoodItem.objects.all()
    return render(request, 'menu/menu.html',{'items': items})

def burgers (request):
    chosen_item = None
    if request.method == "POST":
        item_id = request.POST.get ("item_id")
        chosen_item = item_id
    items = FoodItem.objects.filter(category__name="Burgers")
    return render (request, 'menu/burgers.html', {'items': items, 'chosen_item': chosen_item} )

def pasta (request):
    chosen_item = None
    if request.method == "POST":
        item_id = request.POST.get ("item_id")
        chosen_item = item_id
    items = FoodItem.objects.filter(category__name="Pasta")
    return render (request, 'menu/pasta.html', {'items': items, 'chosen_item': chosen_item} )

def pizza (request):
    chosen_item = None
    if request.method == "POST":
        item_id = request.POST.get ("item_id")
        chosen_item = item_id
    items = FoodItem.objects.filter(category__name="Pizza")
    return render (request, 'menu/pizza.html', {'items': items, 'chosen_item': chosen_item} )

def fish (request):
    chosen_item = None
    if request.method == "POST":
        item_id = request.POST.get ("item_id")
        chosen_item = item_id
    items = FoodItem.objects.filter(category__name="Fish")
    return render (request, 'menu/fish.html', {'items': items, 'chosen_item': chosen_item} )

def soup (request):
    chosen_item = None
    if request.method == "POST":
        item_id = request.POST.get ("item_id")
        chosen_item = item_id
    items = FoodItem.objects.filter(category__name="Soup")
    return render(request, 'menu/soup.html',{'items': items, 'chosen_item': chosen_item} )

def sides (request):
    chosen_item = None
    if request.method == "POST":
        item_id = request.POST.get ("item_id")
        chosen_item = item_id
    items = FoodItem.objects.filter(category__name="Sides")
    return render (request, 'menu/sides.html', {'items': items, 'chosen_item': chosen_item} )

def curry (request):
    chosen_item = None
    if request.method == "POST":
        item_id = request.POST.get ("item_id")
        chosen_item = item_id
    items = FoodItem.objects.filter(category__name="Curry")
    return render (request, 'menu/curry.html', {'items': items, 'chosen_item': chosen_item} )

def vegan (request):
    chosen_item = None
    if request.method == "POST":
        item_id = request.POST.get ("item_id")
        chosen_item = item_id
    items = FoodItem.objects.filter(category__name="Vegan")
    return render (request, 'menu/vegan.html', {'items': items, 'chosen_item': chosen_item} )

def gluten_free (request):
    chosen_item = None
    if request.method == "POST":
        item_id = request.POST.get ("item_id")
        chosen_item = item_id
    items = FoodItem.objects.filter(category__name="Gluten Free")
    return render (request, 'menu/gluten_free.html', {'items': items, 'chosen_item': chosen_item} )

def saver_menu (request):
    chosen_item = None
    if request.method == "POST":
        item_id = request.POST.get ("item_id")
        chosen_item = item_id
    items = FoodItem.objects.filter(category__name="Saver Menu")
    return render (request, 'menu/saver_menu.html', {'items': items, 'chosen_item': chosen_item} )   

def desserts (request):
    chosen_item = None
    if request.method == "POST":
        item_id = request.POST.get ("item_id")
        chosen_item = item_id
    items = FoodItem.objects.filter(category__name="Desserts")
    return render (request, 'menu/desserts.html', {'items': items, 'chosen_item': chosen_item} )

def kids_menu (request):
    chosen_item = None
    if request.method == "POST":
        item_id = request.POST.get ("item_id")
        chosen_item = item_id
    items = FoodItem.objects.filter(category__name="Kids Menu")
    return render (request, 'menu/kids_menu.html',{'items': items, 'chosen_item': chosen_item} )