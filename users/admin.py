from django.contrib import admin
from .models import Profile, Skill

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'email', 'username']
    prepopulated_fields = {'slug': ('first_name', 'last_name')}
    
    
admin.site.register(Skill)


