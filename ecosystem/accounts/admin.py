from django.contrib import admin
from .models import Student, Teacher, Group

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    exclude = ['slug']
    list_display = ['user','phone_number', 'date_of_birth']
    
    # prepopulated_fields = {"slug": ('Username',)}

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    
    exclude = ['slug']
    list_display = ['user','phone_number', 'date_of_birth']
    
    # prepopulated_fields = {"slug": ('Username',)}

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):

    list_display = ['auditorium', 'shcool', 'day','start_time','end_time', 'week_type']