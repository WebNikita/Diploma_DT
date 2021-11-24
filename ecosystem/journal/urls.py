from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

app_name = 'journal'

urlpatterns = [
    path('LK/<str:slug>/', views.LK_View_Student.as_view(), name='LK'),
]