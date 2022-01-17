from django.shortcuts import redirect, render
# from django.contrib.auth.views import LoginView
# from django.contrib.auth import authenticate, login

from django.views.generic import DetailView, ListView, TemplateView
from warehouse.models import Warehouse

# Create your views here.
class Warehouse(TemplateView):

    template_name = 'warehouse/index.html'

    def get_context_data(self, **kwargs):
        # slug = self.kwargs['slug']
        context = super().get_context_data(**kwargs)
        # type_product = Warehouse.objects.get(type)

        context['user_data'] = type

        print(context)

        return context

    # def post(self, request, *args, **kwargs):
    
    #     return render(request, 'base.html')