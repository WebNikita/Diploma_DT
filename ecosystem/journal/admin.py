from django.contrib import admin
from .models import  School_subject




@admin.register(School_subject)
class School_subjectAdmin(admin.ModelAdmin):
    
    list_display = ['name']
    
