from django.urls import path

from .views import create_author, create_category, create_blog_post, update_author,index, list_authors, category_index

app_name = 'blogs'

urlpatterns = [
    path("", index, name="index"),
    path("category/<slug:category_slug>/", category_index, name="category_index"),

    path('create/author/', create_author, name='create_author'),
    path('create/category/', create_category, name='create_category'),
    path('create/post/', create_blog_post, name='create_blog_post'),

    path('update/author/<int:author_id>/', update_author, name='update_author'),

    path('list/author/', list_authors, name='list_authors')

]