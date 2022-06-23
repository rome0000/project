from email import contentmanager
from this import s
from turtle import title
from django.db import models

#create  table
class Post(models.Model):
    title = models.CharField(max_length=155)
    content = models.TextField()
    slug = models.SlugField(max_length=255)

def __str__(self):
    return self.title