from django.shortcuts import render
from django.views.generic import View, ListView
from .models import Price


class PriceView(ListView):
    model = Price
    template_name = 'price.html'
    context_object_name = 'price'