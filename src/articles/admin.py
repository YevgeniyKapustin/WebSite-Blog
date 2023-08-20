from django.contrib import admin

from articles.models import Article, Image


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('cover', 'title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    ...
