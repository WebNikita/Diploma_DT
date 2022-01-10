from django.contrib import admin
from .models import Extradition, Warehouse, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
@admin.register(Extradition)
class ExtraditionAdmin(admin.ModelAdmin):

    exclude = ['user_id']
    list_display = ['name','type', 'cell', 'quantity', 'data']
    
    # prepopulated_fields = {"slug": ('Username',)}

# @admin.register(Shipment)
# class ShipmentAdmin(admin.ModelAdmin):
    
#     # exclude = ['slug']
#     list_display = ['name','type', 'cell', 'quantity', 'data']
    
    # prepopulated_fields = {"slug": ('Username',)}

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    
    exclude = ['slug']
    list_display = ['name','category', 'cell', 'remains', 'created', 'updated']
    list_filter = ['created', 'updated']
    prepopulated_fields = {'slug': ('name',)}