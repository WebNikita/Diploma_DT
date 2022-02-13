from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views.generic import DetailView, ListView, TemplateView

from accounts.models import Student, Teacher
from  accounts.week_type import Week_type


class LK_student_View(TemplateView):

    model = Student
    template_name = 'journal/index.html'
    queryset = Student.objects.all()

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:
            if self.kwargs['type_of_week'] != Week_type.type_of_week():
                return redirect(f"/journal/LK/student/{self.kwargs['slug']}/{Week_type.type_of_week()}")
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        else:
            return redirect("/accounts/login/")


    def get_context_data(self, **kwargs):
        
        DAY_CHOICES = {
            'M':'Понедельник',
            'Tu':'Вторник',
            'W':'Среда',
            'Th':'Четверг',
            'F':'Пятница',
        }

        TYPE_CHOICES = {
            'NUM':'Числитель',
            'DEN':'Знаменатель',
        }
             
        schedule = {}

        slug = self.kwargs['slug']
        type_of_week = self.kwargs['type_of_week']
        context = super().get_context_data(**kwargs)
        user_data = Student.objects.get(slug=slug.lower())
        group_data = user_data.group.all()

        for group in group_data:
            bufer = []
            if type_of_week == group.week_type:
                bufer.append(DAY_CHOICES[group.day])
                bufer.append(group.start_time)
                bufer.append(group.end_time)
                bufer.append(group.auditorium)
                schedule[group.school_subject.name] = bufer

        context['schedule'] = schedule
        context['user_data'] = user_data
        context['week_type'] = TYPE_CHOICES[type_of_week]

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

        return context
