from django.urls import path

from mailing.views import ContactView

urlpatterns = [
    path('', ContactView.as_view(), name='contact')
]
