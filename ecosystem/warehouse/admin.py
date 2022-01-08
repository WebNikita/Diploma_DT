from django.contrib import admin
from .models import Extradition, Shipment, Warehouse

@admin.register(Extradition)
class ExtraditionAdmin(admin.ModelAdmin):

    exclude = ['user_id']
    list_display = ['name','type', 'cell', 'quantity', 'data']
    
    # prepopulated_fields = {"slug": ('Username',)}

@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    
    # exclude = ['slug']
    list_display = ['name','type', 'cell', 'quantity', 'data']
    
    # prepopulated_fields = {"slug": ('Username',)}

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    
    # exclude = ['slug']
    list_display = ['name','type', 'cell', 'quantity', 'data', 'remains']