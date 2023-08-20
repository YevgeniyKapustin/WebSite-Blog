from django.urls import path

from about.views import about

urlpatterns: list[path] = [
    path('', about, name='about'),
]
