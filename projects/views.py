from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from .forms import ProjectForm


def index(request):
    projects = Project.objects.all()
    context = {"projects":projects}
    return render(request, "projects/index.html", context)


def show_project(request, slug):
    project = get_object_or_404(Project, slug=slug)
    context = {"project":project}
    return render(request, "projects/project_detail.html", context)


def create_project(request):
    form = ProjectForm()
    
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("projects")
    
    context = {"form": form}  
    return render(request, "projects/project_form.html", context)


def update_project(request, slug):
    project = get_object_or_404(Project, slug=slug)
    form = ProjectForm(instance=project)
    
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect("projects")
        
    context = {"form":form, "project": project}
    return render(request, "projects/project_form.html", context)


def delete_project(request, slug):
    project = get_object_or_404(Project, slug=slug)
    
    if request.method == "POST":
        project.delete()
        return redirect("projects")
    
    context = {"object": project}
    return render(request, "delete_template.html", context)
    
