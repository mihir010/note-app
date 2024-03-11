from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import NotesRoom

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "username", "password1", "password2"]
        help_texts ={
            'username':None,
            'password1':None,
            'password2':None,
        }

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ["email", "password"]
        
class NotesRoomForm(forms.ModelForm):
    class Meta:
        model = NotesRoom
        fields = ["topic"]