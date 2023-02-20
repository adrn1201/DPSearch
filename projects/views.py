from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Project, Tag
from .forms import ProjectForm, ReviewForm
from .utils import search_projects, paginate_projects


def index(request):
    projects, search_query = search_projects(request) 
    custom_range, projects = paginate_projects(request, projects, 1)
    context = {'projects': projects, 'search_query':search_query, 'custom_range':custom_range}
    return render(request, "projects/index.html", context)


def show_project(request, slug):
    project = get_object_or_404(Project, slug=slug)
    form = ReviewForm()
    
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.project = project
            review.owner = request.user.profile
            review.save()
            
            project.get_vote_count
            if project.slug != slug:
                return redirect('show_project', slug=project.slug)
        
    context = {"project":project, "form":form}
    return render(request, "projects/project_detail.html", context)


@login_required(login_url='login')
def create_project(request):
    profile = request.user.profile
    form = ProjectForm()
    
    if request.method == "POST":
        new_tags = request.POST.get('newTags').replace(',', ' ').split()
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            for tag in new_tags:
                tag, created = Tag.objects.get_or_create(name=tag)
                tag.owner = profile
                project.tags.add(tag)
            
            return redirect("account")
    
    context = {"form": form}  
    return render(request, "projects/project_form.html", context)


@login_required(login_url='login')
def update_project(request, slug):
    profile = request.user.profile
    project = profile.project_set.get(slug=slug)
    form = ProjectForm(instance=project)
    
    if request.method == "POST":
        new_tags = request.POST.get('newTags').replace(',', ' ').split()
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save()
            for tag in new_tags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect("projects")
        
    context = {"form":form, "project": project}
    return render(request, "projects/project_form.html", context)


@login_required(login_url='login')
def delete_project(request, slug):
    profile = request.user.profile
    project = profile.project_set.get(slug=slug)
    
    if request.method == "POST":
        project.delete()
        return redirect("projects")
    
    context = {"object": project}
    return render(request, "delete_template.html", context)
    
