from django.shortcuts import render, redirect
from products.models import Product

# Add product to cart
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1

    request.session['cart'] = cart
    return redirect('cart')

# add cart detail view
def cart_detail(request):
    cart = request.session.get('cart', {})
    products_in_cart = []
    total = 0

    for pid, qty in cart.items():
        try:
            product = Product.objects.get(id=int(pid))
        except Product.DoesNotExist:
            continue  # ⬅️ THIS WAS THE BREAKING POINT

        subtotal = product.price * qty
        total += subtotal

        products_in_cart.append({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'qty': qty,
            'subtotal': subtotal,
            'image': product.image if product.image else None,
        })

    return render(request, 'cart.html', {
        'products': products_in_cart,
        'total': total,
    })

# add checkout view
def checkout(request):
    cart = request.session.get('cart', {})
    products_in_cart = []
    total = 0

    for pid, qty in cart.items():
        try:
            product = Product.objects.get(id=int(pid))
        except Product.DoesNotExist:
            continue

        subtotal = product.price * qty
        total += subtotal

        products_in_cart.append({
            'name': product.name,
            'price': product.price,
            'qty': qty,
            'subtotal': subtotal,
        })

    return render(request, 'checkout.html', {
        'products': products_in_cart,
        'total': total,
    })

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})

    product_id = str(product_id)

    if product_id in cart:
        del cart[product_id]

    request.session['cart'] = cart
    return redirect('cart')



