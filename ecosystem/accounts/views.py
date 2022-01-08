from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from accounts.models import Student, Teacher

from django.views.generic import DetailView, ListView, TemplateView

from .forms import LoginForm, RegistrationForm

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
                    if hasattr(user, 'student'):
                        return  redirect(f'/journal/LK/student/{user.username}')
                    else:
                        return  redirect(f'/journal/LK/teacher/{user.username}')
                else:
                    return redirect('/accounts/login/')
            else:
                return redirect('/accounts/login/')
        else:
            form = LoginForm()

        return redirect('/accounts/login/')
        
class LogOut_View(TemplateView):

    template_name = 'registration/login.html'

    def get(self, request, *args, **kwargs):
        logout(request)
        return(redirect('/accounts/login/'))
        
    
class Registration_View(TemplateView):
    
    template_name = 'registration/registration.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = RegistrationForm

        context['form'] = form

        return context
    

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            
            new_user = User.objects.create_user(username = form_data['login'],first_name = form_data['name'], last_name = form_data['last_name'], email = form_data['email'])
            new_user.set_password(form_data['password'])
            new_user.save()

            new_student = Student()
            new_student.user = new_user
            new_student.date_of_birth = form_data['date_of_birth']
            new_student.phone_number = form_data['phone_number']
            new_student.save()
            
            return(redirect('/accounts/login/'))

        return redirect('/accounts/registration/')
    
