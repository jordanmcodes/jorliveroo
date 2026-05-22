from django.shortcuts import render
from .models import FoodItem

def menu(request):
    items = FoodItem.objects.all()
    return render(request, 'menu/menu.html',{'items': items})

def burgers (request):
    basket = request.session.get('basket', [])
    chosen_item = None
    if request.method == "POST":
        item_id = request.POST.get ("item_id")
        basket.append(item_id)
        request.session['basket'] = basket
        chosen_item = item_id
    items = FoodItem.objects.filter(category__name="Burgers")
    return render (request, 'menu/burgers.html', {'items': items, 'chosen_item': chosen_item} )

def pasta (request):
    basket = request.session.get('basket', [])
    chosen_item = None
    if request.method == "POST":
        item_id = request.POST.get ("item_id")
        basket.append(item_id)
        request.session['basket'] = basket
        chosen_item = item_id
    items = FoodItem.objects.filter(category__name="Pasta")
    return render (request, 'menu/pasta.html', {'items': items, 'chosen_item': chosen_item} )

def pizza (request):
    basket = request.session.get('basket', [])
    chosen_item = None
    if request.method == "POST":
        item_id = request.POST.get ("item_id")
        basket.append(item_id)
        request.session['basket'] = basket
        chosen_item = item_id
    items = FoodItem.objects.filter(category__name="Pizza")
    return render (request, 'menu/pizza.html', {'items': items, 'chosen_item': chosen_item} )

def fish (request):
    basket = request.session.get('basket', [])
    chosen_item = None
    if request.method == "POST":
        item_id = request.POST.get ("item_id")
        basket.append(item_id)
        request.session['basket'] = basket
        chosen_item = item_id
    items = FoodItem.objects.filter(category__name="Fish")
    return render (request, 'menu/fish.html', {'items': items, 'chosen_item': chosen_item} )

def soup (request):
    basket = request.session.get('basket', [])
    chosen_item = None
    if request.method == "POST":
        item_id = request.POST.get ("item_id")
        basket.append(item_id)
        request.session['basket'] = basket
        chosen_item = item_id
    items = FoodItem.objects.filter(category__name="Soup")
    return render (request, 'menu/soup.html', {'items': items, 'chosen_item': chosen_item} )

def sides (request):
    basket = request.session.get('basket', [])
    chosen_item = None
    if request.method == "POST":
        item_id = request.POST.get ("item_id")
        basket.append(item_id)
        request.session['basket'] = basket
        chosen_item = item_id
    items = FoodItem.objects.filter(category__name="Sides")
    return render (request, 'menu/sides.html', {'items': items, 'chosen_item': chosen_item} )

def curry (request):
    basket = request.session.get('basket', [])
    chosen_item = None
    if request.method == "POST":
        item_id = request.POST.get ("item_id")
        basket.append(item_id)
        request.session['basket'] = basket
        chosen_item = item_id
    items = FoodItem.objects.filter(category__name="Curry")
    return render (request, 'menu/curry.html', {'items': items, 'chosen_item': chosen_item} )

def vegan (request):
    basket = request.session.get('basket', [])
    chosen_item = None
    if request.method == "POST":
        item_id = request.POST.get ("item_id")
        basket.append(item_id)
        request.session['basket'] = basket
        chosen_item = item_id
    items = FoodItem.objects.filter(category__name="Vegan")
    return render (request, 'menu/vegan.html', {'items': items, 'chosen_item': chosen_item} )

def gluten_free (request):
    basket = request.session.get('basket', [])
    chosen_item = None
    if request.method == "POST":
        item_id = request.POST.get ("item_id")
        basket.append(item_id)
        request.session['basket'] = basket
        chosen_item = item_id
    items = FoodItem.objects.filter(category__name="Gluten Free")
    return render (request, 'menu/gluten_free.html', {'items': items, 'chosen_item': chosen_item} )

def saver_menu (request):
    basket = request.session.get('basket', [])
    chosen_item = None
    if request.method == "POST":
        item_id = request.POST.get ("item_id")
        basket.append(item_id)
        request.session['basket'] = basket
        chosen_item = item_id
    items = FoodItem.objects.filter(category__name="Saver Menu")
    return render (request, 'menu/saver_menu.html', {'items': items, 'chosen_item': chosen_item} ) 

def desserts (request):
    basket = request.session.get('basket', [])
    chosen_item = None
    if request.method == "POST":
        item_id = request.POST.get ("item_id")
        basket.append(item_id)
        request.session['basket'] = basket
        chosen_item = item_id
    items = FoodItem.objects.filter(category__name="Desserts")
    return render (request, 'menu/desserts.html', {'items': items, 'chosen_item': chosen_item} )

def kids_menu (request):
    basket = request.session.get('basket', [])
    chosen_item = None
    if request.method == "POST":
        item_id = request.POST.get ("item_id")
        basket.append(item_id)
        request.session['basket'] = basket
        chosen_item = item_id
    items = FoodItem.objects.filter(category__name="Kids Menu")
    return render (request, 'menu/kids_menu.html', {'items': items, 'chosen_item': chosen_item} )


def basket (request):
     basket = request.session.get('basket', [])
     if request.method == "POST":
         remove_item = request.POST.get("remove_item")
         checkout=request.POST.get("checkout")
         if checkout:
             address = request.POST.get("address")
             phone = request.POST.get("phone")
             card = request.POST.get("card")
             return render(request, 'menu/basket.html',{'address': address, 'phone': phone, 'checked_out': True})
         if remove_item:
             basket.remove(remove_item)
             request.session['basket'] = basket
         else:
            request.session['basket'] = []
     items = FoodItem.objects.filter(id__in=basket)
     total = 0
     for item in items:
        total+= item.price
     return render (request, 'menu/basket.html', {
         'items': items,
         'total': total
     })