from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User

# Create your models here.

class Tag(Model):
    title = models.CharField(max_length=255)
    
class TaggedItem(Model):
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT, null=False)
    room = models.ManyToManyField('NotesRoom', related_name='tags', blank=True, null=True)

class NotesRoom(Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='rooms')
    topic = models.CharField(max_length=255)

class Note(Model):
    room = models.ForeignKey(NotesRoom, on_delete=models.CASCADE, null=False)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    


