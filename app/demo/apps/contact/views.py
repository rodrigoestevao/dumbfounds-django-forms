from django.shortcuts import render
from django.http import HttpResponse

from . import forms


def contact(request):
    if request.method == "POST":
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            print(name, email)

    form = forms.ContactForm()
    return render(
        request=request,
        template_name="contact/form.html",
        context={"form": form},
    )
