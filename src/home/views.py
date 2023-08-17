from django.views.generic import ListView

from articles.models import Article


class HomeListView(ListView):
    model = Article
    template_name = 'home/home.html'
    context_object_name = 'articles'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context
