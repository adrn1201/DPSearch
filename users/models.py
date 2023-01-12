from django.db import models
from django.contrib.auth.models import User
import uuid
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=320, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    short_intro = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default='profiles/user-default.png')
    social_github = models.CharField(max_length=2048, null=True, blank=True)
    social_twitter = models.CharField(max_length=2048, null=True, blank=True)
    social_linkedin = models.CharField(max_length=2048, null=True, blank=True)
    social_youtube = models.CharField(max_length=2048, null=True, blank=True)
    social_website = models.CharField(max_length=2048, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    
    
    class Meta:
        verbose_name_plural = 'Profiles'  
    
    
    def __str__(self):
        return self.username
    
    
    def get_absolute_url(self):
        return reverse("user-profile", args=[self.slug])
    
    
    @property
    def image_url(self):
        try:
            url = self.profile_image.url
        except:
            url = ''
        return url    
  
    
    @property
    def get_name(self):
        return f"{self.first_name} {self.last_name}"


class Skill(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        verbose_name_plural = 'Skills'  
           
    def __str__(self):
        return self.name