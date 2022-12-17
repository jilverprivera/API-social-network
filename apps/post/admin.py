from django.contrib import admin
from apps.post.models import Image, Post, Comment

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Image)
