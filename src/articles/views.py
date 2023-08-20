from django.views.generic import DetailView

from articles.mixins import ArticleViewCountMixin
from articles.models import Article


class ArticlesDetailView(ArticleViewCountMixin, DetailView):
    model = Article
    template_name = 'articles/article.html'
    context_object_name = 'article'
