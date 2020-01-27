from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from static_pages.models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
# Create your views here.

# when we get a request, we return the corresponding page
class HelloWorld(TemplateView):
    # This time we connect URL with static page
    # function get_template_name()
    template_name='test.html'


# Two views implement Master-detail structure 
# View has relationship with both model and template
# Create class, modify URL and create template
class PostView(ListView):
    model = Post
    template_name = 'index.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


# create update and delete of users' input
class PostCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    #user provide info of all the fields
    fields = '__all__'

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    #user provide info of all the fields
    fields = '__all__'

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    # when execute successfully, jump to the target page
    # cannot delete and jump at the same time
    # so we use reverse_lazy instead of reverse
    success_url = reverse_lazy("posts")
