from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'
