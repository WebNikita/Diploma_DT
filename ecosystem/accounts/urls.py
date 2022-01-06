from django.contrib.auth import views
from django.urls import path
from .views import LogIn_View

app_name = 'accounts'

urlpatterns = [
    path('login/', LogIn_View.as_view(), name='login')
]