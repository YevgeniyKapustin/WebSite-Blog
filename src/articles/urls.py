from django.urls import path

from articles.views import ArticlesDetailView, HomeListView

urlpatterns: list[path] = [
    path('', HomeListView.as_view(), name='home'),
    path('<slug:slug>/', ArticlesDetailView.as_view(), name='article'),
]
