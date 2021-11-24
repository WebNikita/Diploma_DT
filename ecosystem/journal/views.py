from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.views.generic import DetailView, ListView, TemplateView

from .models import User

class LK_View_Student(DetailView):

    # model = Student
    template_name = 'index.html'
    # queryset = Student.objects.all()

    # def get_context_data(self, **kwargs):
    #     slug = self.kwargs['slug']
    #     context = super().get_context_data(**kwargs)
    #     student_data = Student.objects.get(slug=slug)

    #     context['student_data'] = student_data

    #     print(context['student_data'])

    #     return context

class LogIn_View(TemplateView):
    
    template_name = 'login/login.html'

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
                    return HttpResponse('Auth secces')
                else:
                    return HttpResponse('Disabled')
            else:
                return HttpResponse('Invalid login')
        else:
            form = LoginForm()

        return render(request, 'login/login.html', {'form':form})