from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.signup, name='register'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('notes/<str:pk>/', views.notesRoom, name='notes'),
    path('createnotesroom/', views.createNotesRoom, name='createnotesroom'),
    path('editnotesroom/<str:pk>/', views.editNotesRoom, name='editnotesroom'),
    path('deletenotesroom/<str:pk>/', views.deleteNotesRoom, name='deletenotesroom')
]