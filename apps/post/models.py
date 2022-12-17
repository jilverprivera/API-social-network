from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    return 'users/socialposts/{0}'.format(filename)


class Post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='social_post_author')
    image = models.ManyToManyField('Image', blank=True)
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(
        User, blank=True, related_name='dislikes')


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='social_comment_author')
    comment = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(
        User, blank=True, related_name='comment_likes')
    dislikes = models.ManyToManyField(
        User, blank=True, related_name='comment_dislikes')
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True, null=True, related_name='+')

    @property
    def children(self):
        return Comment.objects.filter(parent=self).order_by('-created_on').all()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False


class Image(models.Model):
    image = models.ImageField(
        upload_to=user_directory_path, blank=True, null=True)
