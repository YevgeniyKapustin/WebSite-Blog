from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.SlugField(
        max_length=100, unique=True, db_index=True, verbose_name="slug"
    )
    content = models.TextField(verbose_name='контент')
    cover = models.ImageField(upload_to='covers', verbose_name='обложка')
    views_count = models.TextField(verbose_name='количество просмотров')
    date = models.DateTimeField(auto_now_add=True, verbose_name='дата')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('articlesdetailview', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-date']
