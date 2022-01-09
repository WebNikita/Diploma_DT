from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

app_name = 'journal'

urlpatterns = [
    path('LK/student/<str:slug>/<str:type_of_week>', views.LK_student_View.as_view(), name='LK_student'),
    path('LK/teacher/<str:slug>/<str:type_of_week>', views.LK_teacher_View.as_view(), name='LK_teacher'),
]