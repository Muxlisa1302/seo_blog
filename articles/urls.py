from django.urls import path
from .import views


app_name = 'articles'

urlpatterns = [
    path('author/create/', views.author_create, name='author/create'),
    path('create/', views.article_create, name='create')

]