from django import forms
from .models import Author, Category, BlogPost

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = [ 'bio']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug']

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'slug', 'content', 'author', 'categories', 'related_posts']
