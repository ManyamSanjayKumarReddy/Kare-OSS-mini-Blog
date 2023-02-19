from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog
from .forms import BlogForm

# Create your views here.

# blogs = [
#     {'id': 1, 'name': "Let's Dive into Django documentation."},
#     {'id': 2, 'name': "Hey here is the demo of React Native Setup and Installation."},
#     {'id': 3, 'name': "Complete Beginner guide to Python Basics."},
# ]

def home(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'base/home.html', context)

def blog(request, pk):
    # blog = None
    # for i in blogs:
    #     if i['id'] == int(pk):
    #         blog = i
    
    blog = Blog.objects.get(id=pk)
    context = {'blog': blog}
    return render(request, 'base/blog.html', context)

def createBlog(request):
    form = BlogForm()

    if request.method == 'POST':
        form =BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context={'form': form}
    return render(request, 'base/blog_form.html', context)

def updateBlog(request, pk): 
    blog = Blog.objects.get(id=pk)
    form = BlogForm(instance=blog)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog )
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/blog_form.html', context)

def delete(request, pk):
    blog =Blog.objects.get(id=pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj' : blog})