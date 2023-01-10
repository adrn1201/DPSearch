from django.contrib import admin
from .models import Profile, Skill

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'email', 'username']
    prepopulated_fields = {'slug': ('name',)}
    
    
admin.site.register(Skill)


