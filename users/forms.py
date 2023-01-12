from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Skill

from django.forms import ModelForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name', 
            'last_name', 
            'email', 
            'username', 
            'password1', 
            'password2'
        ]
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields.values():
            field.widget.attrs.update({"class": "input"})
            

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            'first_name', 'last_name', 'email', 
            'username', 'location', 'short_intro', 
            'bio', 'profile_image','social_github',
            'social_twitter','social_linkedin', 
            'social_youtube','social_website'
        ]
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields.values():
            field.widget.attrs.update({"class": "input"})
            
            
class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'description']
        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
        for field in self.fields.values():
            field.widget.attrs.update({"class": "input"})
        