from django.contrib import admin
from django.urls import path,include
import blog.views
urlpatterns = [

    path('', blog.views.blog_index),
    path('create/',blog.views.create_blogpost),
]