from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView

class ProductList(ListView):
    model = Product
    extra_context = {
        'title': 'Store: Minishop'
    }
    template_name = 'store/product_list.html'
