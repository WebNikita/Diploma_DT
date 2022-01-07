from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
# from ..accounts.forms import LoginForm
from django.views.generic import DetailView, ListView, TemplateView

from accounts.models import Student, Teacher

class LK_student_View(TemplateView):

    model = Student
    template_name = 'index.html'
    queryset = Student.objects.all()

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        else:
            return redirect("/accounts/login/")


    def get_context_data(self, **kwargs):
        slug = self.kwargs['slug']
        context = super().get_context_data(**kwargs)
        user_data = Student.objects.get(slug=slug)

        context['user_data'] = user_data

        print(context)

        return context


class LK_teacher_View(TemplateView):

    model = Student
    template_name = 'index.html'
    queryset = Student.objects.all()

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        else:
            return redirect("/accounts/login/")

    def get_context_data(self, **kwargs):
        slug = self.kwargs['slug']
        context = super().get_context_data(**kwargs)
        user_data = Teacher.objects.get(slug=slug)

        context['user_data'] = user_data

        print(context)

        return context

# class LogIn_View(TemplateView):
    
#     template_name = 'login/login.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         form = LoginForm

#         context['form'] = form

#         return context
    
#     def post(self, request, *args, **kwargs):
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             form_data = form.cleaned_data
#             user = authenticate(request,
#                                 username = form_data['login'],
#                                 password = form_data['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return  redirect(f'/journal/LK/{user.username}')
#                 else:
#                     return redirect('/journal/login')
#             else:
#                 return redirect('/journal/login')
#         else:
#             form = LoginForm()

#         return render(request, 'login/login.html', {'form':form})