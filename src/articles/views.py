from django.views.generic import DetailView, ListView

from articles.mixins import ArticleViewCountMixin
from articles.models import Article


class ArticlesDetailView(ArticleViewCountMixin, DetailView):
    model = Article
    template_name = 'articles/article.html'
    context_object_name = 'article'


class HomeListView(ListView):
    model = Article
    template_name = 'articles/home.html'
    context_object_name = 'articles'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Статьи'
        return context
