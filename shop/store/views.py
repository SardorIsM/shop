from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView

class ProductList(ListView):
    model = Product
    context_object_name = 'categories'
    extra_context = {
        'title': 'Store: Minishop'
    }
    template_name = 'store/product_list.html'

    def get_queryset(self):
        categories = Category.objects.filter(parent=None)
        return categories
    
