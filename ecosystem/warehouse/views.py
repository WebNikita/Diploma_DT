from django.shortcuts import redirect, render
# from django.contrib.auth.views import LoginView
# from django.contrib.auth import authenticate, login

from django.views.generic import DetailView, ListView, TemplateView

# Create your views here.
class Warehouse(TemplateView):

    template_name = 'warehouse/index.html'

    # def post(self, request, *args, **kwargs):
    
    #     return render(request, 'base.html')