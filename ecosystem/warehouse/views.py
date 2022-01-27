from re import template
from unicodedata import category, name
from django.shortcuts import redirect, render
from django.template import context
# from django.contrib.auth.views import LoginView
# from django.contrib.auth import authenticate, login

from django.views.generic import DetailView, ListView, TemplateView
from warehouse.models import Warehouse, Category

# Create your views here.
class Warehouse(TemplateView):

    template_name = 'warehouse/index.html'

    def get_context_data(self, **kwargs):
        # slug = self.kwargs['slug']
        context = super().get_context_data(**kwargs)
        category = Category.objects.all()

        context['catalog_list'] = category

        print(context)

        return context

class Catalog(TemplateView):
    
    template_name = 'warehouse/index.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        category_list = Category.objects.all()
        products = Category.objects.get(slug = self.kwargs['slug']).products.all()

        # print(products)

        context['catalog_list'] = category_list
        context['products'] = products
        print(context)

        return context


    # def post(self, request, *args, **kwargs):
    
    #     return render(request, 'base.html')