from django.db import models
from imagekit.models import ProcessedImageField
from django.urls import reverse
# Create your models here.
# define a kind of data "Post", it has two attributes
class Post(models.Model):
    title = models.TextField(blank=True , null=True)
    image = ProcessedImageField(
        #when user upload a image, it will be stored in this path
        upload_to = 'static/images/posts',
        format = 'JPEG',
        options = {'quality': 100},
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title
    
    #when create a post, get the url of target page
    def get_absolute_url(self):
        #get total url from target page nickname
        #self.id is the id of current object
        return reverse("post_detail", args=[str(self.id)])