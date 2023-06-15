from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('register/', views.registerView, name='register'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('', views.homeView, name='home'),
    path('profile/', views.userProfileView, name='profile'),
]