from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Author(models.Model):
    # Estende l'utente base di Django
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # Un post può appartenere a più categorie
    categories = models.ManyToManyField(Category, related_name='blog_posts')
    # Post correlati (self-referential many-to-many)
    related_posts = models.ManyToManyField('self', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# TODO Fare modello Tag qui sotto