
from pyexpat import model
from unicodedata import name
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db.models import Q
from django.urls import resolve

from .form import Order

from django.views.generic import DetailView, ListView, TemplateView
from warehouse.models import Warehouse, Category
from accounts.models import Teacher

# Create your views here.
class Home(TemplateView):

    template_name = 'warehouse/index.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        category = Category.objects.all()
        users = User.objects.all()
        # teacher = Teacher.objects.all()
        # print(teacher)
        print(users)
        form = Order()
        context['form'] = form

        context['catalog_list'] = category
        context['products'] = Warehouse.objects.all()
        context['user'] = users
        context['url'] = resolve(self.request.path_info).url_name
        
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


class SearchResultsView(ListView):
    model = Warehouse
    template_name = 'warehouse/index.html'


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        category_list = Category.objects.all()
        # print(context)
        context['catalog_list'] = category_list
        context['url'] = resolve(self.request.path_info).url_name
        print(context)

        return context


    def get_queryset(self):
        query = self.request.GET.get('search')
        print(query)
        # products = Category.objects.all().product.all()
        # print(products)
        object_list = Warehouse.objects.filter(Q(name__icontains=query) | Q(cell__icontains=query))
        print(object_list)
        
        return object_list

    