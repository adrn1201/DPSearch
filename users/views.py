from django.shortcuts import render, get_object_or_404
from .models import Profile


def index(request):
    profiles = Profile.objects.all()
    context = {"profiles":profiles}
    return render(request, "users/index.html", context)


def show_profile(request, slug):
    profile = get_object_or_404(Profile, slug=slug)
    
    top_skills = profile.skill_set.exclude(description__exact="")
    other_skills = profile.skill_set.filter(description="")
    
    context = {"profile": profile, "top_skills":top_skills, "other_skills":other_skills}
    return render(request, "users/user-profile.html", context)
