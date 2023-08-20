from django import template

from mailing.forms import ContactForm

register = template.Library()


@register.inclusion_tag('mailing/contact_form.html')
def contact_form():
    return {'contact_form': ContactForm()}
