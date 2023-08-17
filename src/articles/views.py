from django.views.generic import ListView, DetailView

from articles.mixins import ArticleViewCountMixin
from articles.models import Article
from articles.services import get_all_articles


class ArticlesListView(ListView):
    model = Article
    template_name = 'articles/articles.html'
    context_object_name = 'articles'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Статьи'
        return context


class ArticlesDetailView(ArticleViewCountMixin, DetailView):
    model = Article
    template_name = 'articles/article.html'
    context_object_name = 'article'
