from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    exclude = ['slug']

    
    
    # prepopulated_fields = {"slug": ('Username',)}
