from django.urls import path
from . import views

# all paths here will have a 'store/' prefix added by ecommerce/urls.py
urlpatterns = [
    path('category/<str:slug>', views.category),
    path('product/<str:slug>', views.product),
]