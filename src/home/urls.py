from django.urls import path

from home.views import HomeListView

urlpatterns: list[path] = [
    path('', HomeListView.as_view(), name='home'),
]
