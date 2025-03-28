from pprint import pprint

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponse, HttpResponseNotAllowed
from django.contrib.auth import get_user_model

from .models import Author, BlogPost, Category
from .forms import AuthorForm, CategoryForm, BlogPostForm, CategorySelectForm


User = get_user_model()

# Create your views here.
def index(request):
    posts = BlogPost.objects.all()[:10]
    category_form = CategorySelectForm(request.GET or None)
    if category_form.is_valid():
        category = category_form.cleaned_data['category']
        return redirect('blogs:category_index', category_slug=category.slug)
    return render(request, 'blogs/index.html', {'posts': posts, 'category_form': category_form} )


def category_index(request, category_slug):
   posts = BlogPost.objects.all().filter(categories__slug=category_slug)
   return render(request, 'blogs/index.html', {'posts': posts} )


## AUTORI ##

def create_author(request):
    # user_qs = User.objects.all().filter(is_staff=False)
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        # form.fields['user'].queryset = user_qs

        if form.is_valid():
            form.save()
            # Redirect a una pagina di conferma o alla lista degli autori
            return redirect('blogs:index')
    else:
        form = AuthorForm()
        # form.fields['user'].queryset = user_qs
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

def list_authors(request):
    if request.method == 'GET':
        queryset = Author.objects.all()
        return render(request, 'blogs/list_author.html', {'titolo': 'Lista Autori', 'queryset': queryset})
    
    return HttpResponseNotAllowed(['POST'])


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