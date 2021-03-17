from django import forms

from django.utils.translation import ugettext_lazy as _

from . import models


class SnippetForm(forms.ModelForm):
    class Meta:
        model = models.Snippet
        fields = (
            "name",
            "body",
        )
