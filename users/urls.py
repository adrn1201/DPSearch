from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),
    
    path('', views.index, name="profiles"),
    path('profile/<slug:slug>', views.show_profile, name="user-profile"),
    
    path('account/', views.show_user_account, name="account"),
    path('account/edit', views.edit_account, name="edit-account"),
]
