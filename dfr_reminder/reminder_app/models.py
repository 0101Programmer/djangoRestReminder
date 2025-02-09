import datetime

from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=250)
    birthdate = models.DateField()
    avatar = models.ImageField(upload_to="static/media/avatars", default="static/media/avatars/cat_developer.jpg")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True, max_length=500)
    image = models.ImageField(upload_to="static/media/notes", null=True, blank=True)
    remind_date = models.DateTimeField(null=True, blank=True, help_text="Пример: 2025-02-09 22:10")
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
