from django.urls import path
from . import views

urlpatterns = [
    path("projects/", views.index, name="projects"),
]
