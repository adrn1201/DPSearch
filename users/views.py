from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.models import User
from .models import Profile

from .forms import CustomUserCreationForm, ProfileForm


def login_user(request):
    
    if request.user.is_authenticated:
        return redirect('profiles')
    
    if request.method == "POST":
        username = request.POST['username'].lower()
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username)
        except:
            pass
        
        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            return redirect('profiles')
        else:
            pass
        
    return render(request, "users/login_register.html")


def logout_user(request):
    logout(request)
    return redirect('login')


def register_user(request):
    page = "register"
    form = CustomUserCreationForm()
    
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            
            login(request, user)
            
            return redirect('profiles')
        else:
            pass
    
    context = {"page": page, "form" : form}
    return render(request, "users/login_register.html", context)
    


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


def show_user_account(request):
    profile = request.user.profile
    
    skills = profile.skill_set.all()
    
    context = {"profile":profile, "skills":skills}
    return render(request, "users/account.html", context)


def edit_account(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')
    
    context = {"form": form}
    return render(request, "users/edit-account.html", context)
