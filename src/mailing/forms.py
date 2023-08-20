from django import forms

from mailing.models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ("email",)
        widgets = {
            "email": forms.TextInput(
                attrs={
                    "class": "editContent",
                    "placeholder": "Your Email..."
                }
            )
        }
        labels = {
            "email": 'Подписка на рассылку!'
        }
