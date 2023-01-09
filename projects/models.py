from django.db import models
import uuid
from django.urls import reverse


class Project(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True)
    demo_link = models.CharField(max_length=2048, null=True, blank=True)
    source_link = models.CharField(max_length=2048, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    class Meta:
        verbose_name_plural = 'Projects'
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("project-detail", args=[self.slug])
    

class Tag(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
     
    class Meta:
        verbose_name_plural = 'Tags'
         
    def __str__(self):
        return self.name