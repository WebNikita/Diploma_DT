from django.contrib.auth import views
from django.urls import path
from .views import Warehouse

app_name = 'warehouse'

urlpatterns = [
    path('', Warehouse.as_view())
]