from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile

from .forms import CustomUserCreationForm, ProfileForm, SkillForm, MessageForm
from .utils import search_profiles, paginate_profiles


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
            return redirect(request.GET['next'] if 'next' in request.GET else 'account')
        else:
            pass
        
    return render(request, "users/login_register.html")


@login_required(login_url='login')
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
            
            return redirect('edit-account')
        else:
            pass
    
    context = {"page": page, "form" : form}
    return render(request, "users/login_register.html", context)
    

def index(request):
    profiles, search_query = search_profiles(request)
    custom_range, profiles = paginate_profiles(request, profiles, 9)
    context = {'profiles': profiles, 'search_query': search_query, 'custom_range':custom_range}
    return render(request, "users/index.html", context)


def show_profile(request, slug):
    profile = get_object_or_404(Profile, slug=slug)
    
    top_skills = profile.skill_set.exclude(description__exact="")
    other_skills = profile.skill_set.filter(description="")
    
    context = {"profile": profile, "top_skills":top_skills, "other_skills":other_skills}
    return render(request, "users/user-profile.html", context)


@login_required(login_url='login')
def show_user_account(request):
    profile = request.user.profile
    
    skills = profile.skill_set.all()
    projects = profile.project_set.all()
    
    context = {"profile":profile, "skills":skills, "projects":projects}
    return render(request, "users/account.html", context)


@login_required(login_url='login')
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


@login_required(login_url='login')
def create_skill(request):
    profile = request.user.profile
    form = SkillForm()
    
    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            
            return redirect('account')
    
    context = {"form":form}
    return render(request, "users/skill_form.html", context)


@login_required(login_url='login')
def edit_skill(request, pk):
    profile = request.user.profile 
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)
    
    if request.method == "POST":
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            
            return redirect('account')
    
    context = {"form": form}
    return render(request, "users/skill_form.html", context)


@login_required(login_url='login')
def delete_skill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    
    if request.method == "POST":
        skill.delete()
        return redirect('account')
    
    context = {"object":skill}
    return render(request, "delete_template.html", context)


@login_required(login_url='login')
def show_inbox(request):
    profile = request.user.profile
    messages = profile.messages.all()
    unread_count = profile.messages.filter(is_read=False).count()
    
    context = {"messages":messages, "unread_count":unread_count}     
    return render(request, "users/inbox.html", context)  


@login_required(login_url='login')
def view_message(request, pk):
    profile = request.user.profile
    message = profile.messages.get(id=pk)
    
    if not message.is_read:
        message.is_read = True
        message.save()
        
    context = {"message":message}
    return render(request, "users/message.html", context)


@login_required(login_url='login')
def create_message(request, pk):
    recipient = Profile.objects.get(id=pk)
    form = MessageForm()
    
    try:
        sender = request.user.profile
    except:
        sender = None
        
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender 
            message.recipient = recipient
            
            if sender:
                message.name = sender.get_name
                message.email = sender.email
            
            message.save()
            return redirect('user-profile', slug=recipient.slug)

    context = {"form": form, "recipient":recipient}
    return render(request, "users/message_form.html", context) 
    
