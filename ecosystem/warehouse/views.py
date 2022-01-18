from django.shortcuts import redirect, render
# from django.contrib.auth.views import LoginView
# from django.contrib.auth import authenticate, login

from django.views.generic import DetailView, ListView, TemplateView
from warehouse.models import Warehouse, Category

# Create your views here.
class Warehouse(TemplateView):

    template_name = 'warehouse/index.html'

    def get_context_data(self, **kwargs):
        slug = self.kwargs['views']
        context = super().get_context_data(**kwargs)
        print(context)
        user_data = Category.objects.get(slug=slug)

        context['user_data'] = user_data


        return context

    # def post(self, request, *args, **kwargs):
    
    #     return render(request, 'base.html')