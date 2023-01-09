from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="projects"),
    path("new/", views.create_project, name="create-project"),
    path("<slug:slug>/", views.show_project, name="project-detail"),
    path("<slug:slug>/edit/", views.update_project, name="update-project"),
    path("<slug:slug>/delete/", views.delete_project, name="delete-project"),
]
