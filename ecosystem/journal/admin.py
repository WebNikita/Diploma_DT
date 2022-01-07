from django.contrib import admin
from .models import Group, School_subject


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):

    list_display = ['auditorium', 'shcool']

@admin.register(School_subject)
class School_subjectAdmin(admin.ModelAdmin):
    
    list_display = ['name','day','start_time','end_time', 'week_type']
    
