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
        ordering = ['-vote_ratio', '-vote_total', 'title']
       
        
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
    
    
    @property
    def reviewers(self):
        queryset = self.review_set.all().values_list('owner__id', flat=True)
        return queryset
    
    
    @property
    def get_vote_count(self):
        reviews = self.review_set.all()
        up_votes = reviews.filter(value='up').count()
        total_votes = reviews.count()
        
        ratio = (up_votes / total_votes) * 100
        self.vote_total = total_votes
        self.vote_ratio = ratio
        self.save()
    
    
class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote')
    )
    
    owner = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    value = models.CharField(max_length=255, choices=VOTE_TYPE)
    body = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    
    class Meta:
        unique_together = [['owner', 'project']]
        verbose_name_plural = 'Reviews'
    
    
    def __str__(self):
        return self.value

    
class Tag(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
     
    class Meta:
        verbose_name_plural = 'Tags'
         
    def __str__(self):
        return self.name