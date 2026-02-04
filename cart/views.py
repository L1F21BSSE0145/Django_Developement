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

