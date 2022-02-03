from unicodedata import name
from django.contrib.auth import views
from django.urls import path

# from ecosystem.warehouse.models import Category
from .views import Warehouse, Catalog, SearchResultsView

app_name = 'warehouse'

urlpatterns = [
    path('', Warehouse.as_view(), name='warehouse'),
    path('search/',SearchResultsView.as_view(), name='search_product'),
    path('<str:slug>/', Catalog.as_view(), name='render_catalog'),
]