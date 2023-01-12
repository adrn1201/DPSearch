from django.db import models
import uuid
from django.urls import reverse

from users.models import Profile

class Project(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    featured_image = models.ImageField(null=True, blank=True, default='default.jpg')
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
    
    def get_edit_url(self):
        return reverse("update-project", args=[self.slug])
    
    def get_delete_url(self):
        return reverse("delete-project", args=[self.slug])
    
    @property
    def image_url(self):
        try:
            url = self.featured_image.url
        except:
            url = ''
        return url
    

class Tag(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
     
    class Meta:
        verbose_name_plural = 'Tags'
         
    def __str__(self):
        return self.name