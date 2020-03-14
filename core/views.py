from django.contrib import messages
from django.shortcuts import (
    render, get_object_or_404, redirect
)
from .models import *
from django.views.generic import (
    ListView, DetailView
)
from django.utils import timezone


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
    order_item = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False)
    order_qs = Order.objects.filter(
        user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(
                request, "Item quantity Updated")
        else:
            messages.info(
                request, "Item added to Cart")
            order.times.add(order_item)
            return redirect("core:product", slug=slug)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, 
            ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(
            request, "Item added to Cart")
    return redirect("core:product", slug=slug)


def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(item=item, user=request.user, ordered=False)
            order.times.remove(order_item)
            messages.info(
                request, "Item removed from cart")
            return redirect("core:product", slug=slug)
        else:
            messages.info(
                request, "Item not in your cart")
            return redirect("core:product", slug=slug)
    else:
        messages.info(
            request, "You do not have an active order")
        return redirect("core:product", slug=slug)
