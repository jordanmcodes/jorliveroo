from django.shortcuts import render
from .models import FoodItem
    # Used for displaying all the food on the main menu.
def menu(request):
        items = FoodItem.objects.all()
        return render(request, 'menu/menu.html',{'items': items})

    # Burgers are added to the basket from this section, displaying their price and name.
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

    # Pasta is added to the basket from this section, displaying their price and name.

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

    # Pizzas are added to the basket from this section, displaying their price and name.

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

    # Fish items are added to the basket from this section, displaying their price and name.

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

    # Soups are added to the basket from this section, displaying their price and name.

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

    # Sides are added to the basket from this section, displaying their price and name.

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

    # Curry items are added to the basket from this section, displaying their price and name.

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

    # Vegan items are added to the basket from this section, displaying their price and name.

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

    # Gluten free items are added to the basket from this section, displaying their price and name.

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

    # Saver menu items are added to the basket from this section, displaying their price and name.

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

    # Desserts are added to the basket from this section, displaying their price and name.

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

    # Kids items are added to the basket from this section, displaying their price and name.

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

    # Handles the baskets functionality including removing items, checking out, and calculating the total price.
def basket (request):
        basket = request.session.get('basket', [])
        if request.method == "POST":
            remove_item = request.POST.get("remove_item")
            checkout=request.POST.get("checkout")
            add_item= request.POST.get("add_item")
            if checkout:
                address = request.POST.get("address")
                phone = request.POST.get("phone")
                card = request.POST.get("card")
                return render(request, 'menu/basket.html',{'address': address, 'phone': phone, 'checked_out': True})
            if remove_item:
                basket.remove(remove_item)
                request.session['basket'] = basket
            elif add_item:
                  basket.append(add_item)
                  request.session['basket'] = basket
            else:
                request.session['basket'] = []
        items = []
        for item_id in basket:
              items.append(FoodItem.objects.get(id=item_id))
        total = 0
        for item in items:
            total+= item.price

        total = round(total,2)
        return render (request, 'menu/basket.html', {
        'items': items,
        'total': total
         })