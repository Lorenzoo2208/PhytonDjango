from pprint import pprint

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponse

from .models import Author
from .forms import AuthorForm, CategoryForm, BlogPostForm

# Create your views here.
def index(request):
    return render(request, 'blogs/index.html', {'title': 'implementa tu la home page'} )


## AUTORI ##

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


def update_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
    else:
        form = AuthorForm(instance=author)
    
    return render(request, 'blogs/update_author.html', {'form': form, 'author': author})

## TODO ## Fare lista categorie


## CATEGORIE ##

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