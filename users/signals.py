from django.contrib.auth.models import User
from .models import Profile

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.core.mail import send_mail
from django.conf import settings

import string 
from django.utils.text import slugify 
import random 


def random_string_generator(size = 10, chars = string.ascii_lowercase + string.digits): 
    return ''.join(random.choice(chars) for _ in range(size)) 
   

def unique_slug_generator(instance, new_slug = None): 
    if new_slug is not None: 
        slug = new_slug 
    else: 
        slug = slugify(instance.get_name) 
    class_instance = instance.__class__ 
    qs_exists = class_instance.objects.filter(slug = slug).exists() 
      
    if qs_exists: 
        new_slug = "{slug}-{randstr}".format( 
            slug = slug, randstr = random_string_generator(size = 4)) 
              
        return unique_slug_generator(instance, new_slug = new_slug) 
    return slug 


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            first_name = user.first_name,
            last_name = user.last_name  
        )
        
        if not profile.slug:
            profile.slug = unique_slug_generator(profile) 
            profile.save()

