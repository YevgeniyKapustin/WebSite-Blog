from django.views.generic import ListView, DetailView

from articles.models import Article


class ArticlesListView(ListView):
    model = Article
    template_name = 'articles/articles.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Статьи'
        context['articles'] = Article.objects.all()
        return context


class ArticlesDetailView(DetailView):
    model = Article
    template_name = 'articles/article.html'
