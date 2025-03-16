from pprint import pprint

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponse

from .forms import AuthorForm, CategoryForm, BlogPostForm

# Create your views here.
def index(request):
    return HttpResponse("index")


def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect a una pagina di conferma o alla lista degli autori
            return redirect('blogs:index')
    else:
        form = AuthorForm()
    return render(request, 'blogs/create_author.html', {'form': form})


def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect a una pagina di conferma o alla lista delle categorie
            return redirect('blogs:index')
    else:
        form = CategoryForm()
    return render(request, 'blogs/create_category.html', {'form': form})


def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect a una pagina di conferma o alla lista dei post
            return redirect('blogs:index')
    else:
        form = BlogPostForm()
    return render(request, 'blogs/create_blog_post.html', {'form': form})