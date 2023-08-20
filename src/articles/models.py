import math

from django.db import models
from django.urls import reverse

from articles.utils import get_count


class Article(models.Model):
    title: str = models.CharField(max_length=100, verbose_name='заголовок')
    slug: str = models.SlugField(max_length=100, unique=True, db_index=True,
                                 verbose_name="slug")
    content: str = models.TextField(verbose_name='контент статьи в markdown')
    cover = models.ImageField(upload_to='covers', verbose_name='обложка')
    date = models.DateTimeField(auto_now_add=True, verbose_name='дата')
    is_published = models.BooleanField(default=False, verbose_name='дата')

    def __str__(self):
        return self.title

    def get_views_count(self):
        return get_count(self, 'views')

    def get_absolute_url(self):
        return reverse('articlesdetailview', kwargs={'slug': self.slug})

    def get_reading_time(self):
        return math.ceil(len(self.content.split()) / 200)  # avg reading speed

    class Meta:
        ordering = ['-date']


class ViewCount(models.Model):
    article = models.ForeignKey(
        'Article',
        on_delete=models.CASCADE,
        related_name='views'
    )
    ip_address = models.GenericIPAddressField(
        verbose_name='ip адрес'
    )


class Image(models.Model):
    img = models.ImageField(upload_to='img', verbose_name='изображение')
