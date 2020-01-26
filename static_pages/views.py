from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

# when we get a request, we return the corresponding page
class HelloWorld(TemplateView):
    # This time we connect URL with static page
    # function get_template_name()
    template_name='test.html'
