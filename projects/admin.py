from django.contrib import admin
from .models import Project, Tag


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'vote_ratio', 'vote_total']
    list_filter = ['vote_ratio', 'vote_total']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Tag)
    
    