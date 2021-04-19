from django.shortcuts import render, redirect
from django.http import HttpResponse

from store.forms import RegisterForm
from store.models import Category, Product


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
