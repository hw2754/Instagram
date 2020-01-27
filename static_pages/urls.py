"""instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# This is the local view setting (app level)
from django.contrib import admin
from django.urls import include, path
from static_pages.views import HelloWorld,PostView,PostDetailView
from static_pages.views import PostCreateView,PostUpdateView,PostDeleteView
urlpatterns = [
    path('',HelloWorld.as_view(), name='helloworld'),
    path('posts/',PostView.as_view(), name='posts'),
    #find the detail info of image with id(primary key) = pk
    path('posts/<int:pk>/',PostDetailView.as_view(), name='post_detail'),
    path('posts/new/',PostCreateView.as_view(), name='new_post'),
    path('posts/update/<int:pk>/',PostUpdateView.as_view(), name='update_post'),
    path('posts/delete/<int:pk>/',PostDeleteView.as_view(), name='delete_post'),
]
