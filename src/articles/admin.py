from django.contrib import admin

from articles.models import Article, ViewCount


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ViewCount)
class ViewCountAdmin(admin.ModelAdmin):
    ...
