from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import Note, NotesRoom, Tag, TaggedItem
# from django.contrib.auth.forms import UserCreationForm
from . import forms

# Create your views here.

def home(request):
    user = request.user
    notes = user.rooms.all()
    context = {'notes':notes}
    return render(request, 'base/home.html', context)

def notesRoom(request, pk):
    user = request.user
    notesroom = user.rooms.get(id=pk)
    notes = notesroom.note_set.all()
    context = {'notes':notes}
    
    if request.method == "POST":
        note = Note.objects.create(
            room = notesroom,
            text = request.POST.get('body')
        )
        return HttpResponseRedirect(request.path_info)
        
    
    return render(request, 'base/notesroom.html', context)

def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = forms.RegistrationForm()
    context = {'form':form, 'page':'signup'}
    
    if request.method == "POST":
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            HttpResponse("error while saving user")
    
    return render(request, 'base/login_signup.html', context)

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    form = forms.LoginForm()
    context = {'form':form}
    
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # print(username, "-->", password)
            user = None
            try: 
                user = authenticate(request, username=username, password=password)
            except Exception as e:
                print(e)
                
            if user != None:
                login(request, user)
                return redirect('home')
            else:
                print(user)
    
    return render(request, 'base/login_signup.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def createNotesRoom(request):
    notesroomform = forms.NotesRoomForm()
    page = 'create'
    context = {'page': page, 'form': notesroomform}
    
    if request.method == "POST":
        notesroomform = forms.NotesRoomForm(request.POST)
        if notesroomform.is_valid():
            notesroom = notesroomform.save(commit=False)
            notesroom.author = request.user
            notesroom.save()
            return redirect('notes', pk=notesroom.id)
        else:
            notesroomform = forms.NotesRoom(request.POST)
            return redirect('createnotes')
    
    return render(request, "base/edit_create_room.html", context)

def editNotesRoom(request, pk):
    notesroom = NotesRoom.objects.get(id=pk)
    notesroomform = forms.NotesRoomForm(instance=notesroom)
    page = 'edit'
    form = notesroomform
    context = {'page':page, 'form':form}
    
    if request.method == "POST":
        notesroom = forms.NotesRoomForm(request.POST, instance=notesroom)
        if notesroom.is_valid():
            notesroom.save()
            return redirect('home')
        else:
            notesroom = forms.NotesRoomForm(request.POST)
            return redirect('editnotesroom')
    
    return render(request, 'base/edit_create_room.html', context)
    
def deleteNotesRoom(request, pk):
    notesroom = NotesRoom.objects.get(id=pk)
    context = {'room':notesroom}
    
    if request.method == "POST":  
        try:
            notesroom.delete()
            return redirect('home')
        except Exception as e:
            print(e)
    
    return render(request, 'base/delete_room.html', context)