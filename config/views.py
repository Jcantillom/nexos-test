from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from src.product.models import Product, Inventory


class HomeView(TemplateView):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        inventories = Inventory.objects.all()
        return render(request,
                      'index.html',
                      {'products': products, 'inventories': inventories}
                      )
