from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'store/index.html')


def category(request, slug):
    return HttpResponse("Category " + slug)


def product(request, slug):
    return HttpResponse("Product " + slug)