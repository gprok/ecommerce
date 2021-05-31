from django.shortcuts import render, redirect
from django.http import HttpResponse

from store.forms import RegisterForm
from store.models import Category, Product, Cart, Items


def index(request):
    context = {'categories': Category.objects.all().order_by('name')}
    return render(request, 'store/index.html', context)


def category(request, slug):
    slug = slug.lower()
    category = Category.objects.filter(slug=slug).first()
    context = {'categories': Category.objects.all().order_by('name'),
               'category': category,
               'products': Product.objects.filter(category=category.id)}
    return render(request, 'store/category.html', context)


def product(request, slug):
    slug = slug.lower()
    context = {'categories': Category.objects.all().order_by('name'),
               'product': Product.objects.filter(slug=slug).first()}
    return render(request, 'store/product.html', context)


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = RegisterForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)


def cart(request):
    txt = ""

    # Find cart in DB
    session_id = request.session.session_key
    if not session_id:
        request.session.create()
        session_id = request.session.session_key

    try:
        cart = Cart.objects.get(session_id=session_id)
    except Cart.DoesNotExist:
        cart = Cart()
        cart.session_id = session_id
        cart.save()

    # Find items of the cart
    items = Items.objects.filter(cart=cart)
    for item in items:
        txt += item.product.slug + ": " + str(item.quantity) + "<br>"

    context = {
        'items': items,
        'categories': Category.objects.all().order_by('name'),
    }

    return render(request, 'store/cart.html', context)


def add_to_cart(request, product_id):
    # Open cart or Create cart
    session_id = request.session.session_key
    if not session_id:
        request.session.create()
        session_id = request.session.session_key

    try:
        cart = Cart.objects.get(session_id=session_id)
    except Cart.DoesNotExist:
        cart = Cart()
        cart.session_id = session_id
        cart.save()

    # get item from DB
    product = Product.objects.get(id=product_id)

    # add item to cart OR increase quantity if already in cart
    try:
        item = Items.objects.get(product=product, cart=cart)
        item.quantity += 1
        item.save()
    except Items.DoesNotExist:
        item = Items()
        item.cart = cart
        item.quantity = 1
        item.product = product
        item.save()

    # redirect to cart
    return redirect('/store/cart')


def delete_from_cart(request, product_id):
    print("Deleting Item ", product_id)
    # 1. Get session id
    # 2. Get cart from DB
    # 3. If cart exists,
    # 4. Find product
    # 5. Find Item belonging to this cart with this product
    # 6. If Item exists, Delete Item
    # redirect to cart
    return redirect('/store/cart')


def paypal(request):
    pass