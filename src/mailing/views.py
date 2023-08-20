from django.views.generic import CreateView

from mailing.forms import ContactForm
from mailing.models import Contact


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = '/'
