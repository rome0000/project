from email import contentmanager
from email.policy import default
from this import s
from turtle import title
from django.db import models

#create  table
class Post(models.Model):
    title = models.CharField(max_length=155)
    content = models.TextField()
    slug = models.SlugField(max_length=255)
    image = models.ImageField(upload_to="images/",default="images/default.png")

def __str__(self):
    return self.title