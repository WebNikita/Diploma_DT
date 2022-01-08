from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login

from django.views.generic import DetailView, ListView, TemplateView

from .forms import LoginForm

class LogIn_View(TemplateView):
    
    template_name = 'registration/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = LoginForm

        context['form'] = form

        return context
    
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            user = authenticate(request,
                                username = form_data['login'],
                                password = form_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return  redirect(f'/journal/LK/{user.username}')
                else:
                    return redirect('/accounts/login/')
            else:
                return redirect('/accounts/login/')
        else:
            form = LoginForm()

        return redirect('/accounts/login/')
 