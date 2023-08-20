from django.contrib import admin

from articles.models import Article, ViewCount


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('cover', 'title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
