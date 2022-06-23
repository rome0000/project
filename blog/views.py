from django.shortcuts import render
from .models import Post
def home(request):
    data = Post.objects.all()
    return render(request, "index.html",{"posts":data})
