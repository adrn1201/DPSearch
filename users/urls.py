from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="profiles"),
    path('profile/<slug:slug>', views.show_profile, name="user-profile"),
]
