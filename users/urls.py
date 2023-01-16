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
    
    path('account/skills/new', views.create_skill, name="create-skill"),
    path('account/skills/<str:pk>/edit', views.edit_skill, name="edit-skill"),
    path('account/skills/<str:pk>/delete', views.delete_skill, name="delete-skill"),
    
    path('inbox/', views.show_inbox, name="inbox"),
    path('inbox/messages/new/<str:pk>', views.create_message, name="create_message"),
]
