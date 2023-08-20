from django.urls import path

from articles.views import ArticlesListView, ArticlesDetailView

urlpatterns: list[path] = [
    path('<slug:slug>/', ArticlesDetailView.as_view(), name='article'),
]
