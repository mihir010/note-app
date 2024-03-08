from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.signup, name='register'),
    path('login/', views.loginUser, name='login'),
]