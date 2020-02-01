from django.db import models
from imagekit.models import ProcessedImageField
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class InstaUser(AbstractUser):
    profile_img = ProcessedImageField(
        #when user upload a image, it will be stored in this path
        upload_to = 'static/images/profiles',
        format = 'JPEG',
        options = {'quality': 100},
        blank=True,
        null=True,
    )

# Create your models here.
# define a kind of data "Post", it has two attributes
class Post(models.Model):
    author = models.ForeignKey(
        # we need to put class InstaUser at first
        InstaUser,
        on_delete = models.CASCADE,
        related_name = 'my_posts',
    )
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

class Like(models.Model):
    # relation between Post and InstaUser 
    # Foreign key in the relational database
    # related_name is used to find all the related objects under given foreignkey
    # eg: for a Post, use 'likes' can find all the users like it
    # eg: for a InstaUser, use 'likes' can find all the posts the user likes
    post = models.ForeignKey(
        Post,
        on_delete = models.CASCADE,
        related_name = 'likes')
    user = models.ForeignKey(
        InstaUser,
        on_delete = models.CASCADE,
        related_name = 'likes')
    class Meta:
        unique_together = ("post","user")
    
    def __str__(self):
        return 'Like: ' + self.user.username + ' ' + self.post.title
    

class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete = models.CASCADE,
        related_name = 'comments')

    user = models.ForeignKey(
        InstaUser,
        on_delete = models.CASCADE)

    comment = models.CharField(max_length=100)
    posted_on = models.DateTimeField(auto_now_add=True,editable=False)
    
    def __str__(self):
        return self.comment
