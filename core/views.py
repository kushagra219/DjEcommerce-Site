from django.shortcuts import (
    render, get_object_or_404
)
from .models import *
from django.views.generic import (
    ListView, DetailView
)
# Create your views here.


class HomeView(ListView):
    model = Item
    template_name = 'home-page.html'


class ProductView(DetailView):
    model = Item
    template_name = 'product-page.html'


class CheckoutView(ListView):
    template_name = 'checkout-page.html'


def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item = OrderItem.objeects.create(item=item)