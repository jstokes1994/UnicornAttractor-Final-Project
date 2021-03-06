from django.shortcuts import render, redirect, reverse

# Create your views here.
def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html")

    
def add_to_cart(request, id):
    """Add a quantity of the specified feature to the cart"""
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity   
    else:
        cart[id] = cart.get(id, quantity) 

    request.session['cart'] = cart
    return redirect(reverse('features'))

def remove_from_cart(request, id):
    """Remove an item from the cart"""
    
    cart = request.session.get('cart', {})
    
    if id in cart:
        cart.pop(id)
        print(cart)
    else:
        print("could not do this")
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
        


def adjust_cart(request, id):
    """
    Adjust the quantity of the specified feature to the specified
    amount
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))