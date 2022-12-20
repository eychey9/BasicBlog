from multiprocessing import context
from django.shortcuts import render

from .models import BlogPost


def home(request):
    post = BlogPost.objects.all()
    context = { 'posts': post }
    return render(request, 'home.html', context)   
