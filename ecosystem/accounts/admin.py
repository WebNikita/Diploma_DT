from django.contrib import admin
from .models import Student, Teacher

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
