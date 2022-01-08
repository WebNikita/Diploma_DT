from django.contrib.auth import views
from django.urls import path
from .views import LogIn_View, LogOut_View, Registration_View

app_name = 'accounts'

urlpatterns = [
    path('login/', LogIn_View.as_view(), name='login'),
    path('logout/', LogOut_View.as_view(), name='logout'),
    path('registration/', Registration_View.as_view(), name='registration'),
]