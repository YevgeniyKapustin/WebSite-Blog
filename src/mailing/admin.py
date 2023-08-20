from django.contrib import admin

from articles.models import Article, Image
from mailing.models import Contact


@admin.register(Contact)
class ImageAdmin(admin.ModelAdmin):
    ...
