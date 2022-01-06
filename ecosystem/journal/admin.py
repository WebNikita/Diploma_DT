from django.contrib import admin
from .models import Profile, School_subject


# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):

#     exclude = ['slug']
#     list_display = ['user','type_of_user']

# @admin.register(School_subject)
# class School_subjectAdmin(admin.ModelAdmin):
#     list_display = ['name','day','time', 'classroom']
    
    # prepopulated_fields = {"slug": ('Username',)}
