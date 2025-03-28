
# Register your models here.
from django.contrib import admin
from .models import Author, Category, BlogPost

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')
    search_fields = ('user__username', 'bio')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ('name',)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('author', 'categories')
    search_fields = ('title', 'content')
    filter_horizontal = ('categories', 'related_posts')
