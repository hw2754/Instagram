from django.db import models
from imagekit.models import ProcessedImageField
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