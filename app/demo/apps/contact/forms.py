from django import forms

from django.utils.translation import ugettext_lazy as _

from . import models


class ContactForm(forms.Form):
    name = forms.CharField(label=_("Name"))
    email = forms.EmailField(label=_("E-Mail"))
    category = forms.ChoiceField(
        choices=[
            ("question", _("Question")),
            ("other", _("Other")),
        ]
    )
    subject = forms.CharField(label=_("Subject"), required=False)
    body = forms.CharField(label=_("Body"), widget=forms.Textarea)
