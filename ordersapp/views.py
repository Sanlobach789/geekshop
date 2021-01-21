from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from ordersapp.models import Order


class OrderList(ListView):
    model = Order

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

class OrderItemsCreate(CreateView):
    model = Order
    fields = []
    success_url = reverse_lazy('order:orders_list')
