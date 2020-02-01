from django.contrib import admin

# Register your models here.
from static_pages.models import Post,InstaUser, Like

#register Post model for admin app
admin.site.register(Post)
admin.site.register(InstaUser)
admin.site.register(Like)