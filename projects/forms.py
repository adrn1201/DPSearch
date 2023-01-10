from django.forms import ModelForm
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            'title', 
            'featured_image',
            'description', 
            'demo_link', 
            'source_link'
        ]
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields.values():
            field.widget.attrs.update({"class": "input"})
    