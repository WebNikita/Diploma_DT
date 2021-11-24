from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView

from .models import Student, Teacher, School_subject, Group, Turnout

class LK_View_Student(DetailView):

    model = Student
    template_name = 'index.html'
    queryset = Student.objects.all()

    def get_context_data(self, **kwargs):
        slug = self.kwargs['slug']
        context = super().get_context_data(**kwargs)
        student_data = Student.objects.get(slug=slug)

        context['student_data'] = student_data

        print(context['student_data'])

        return context