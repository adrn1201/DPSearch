from django.contrib import admin
from .models import Project, Review, Tag


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'vote_ratio', 'vote_total']
    list_filter = ['vote_ratio', 'vote_total']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['owner', 'project', 'value']


admin.site.register(Tag)
    
    