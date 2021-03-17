from django.shortcuts import render

from . import forms


def snippet(request):
    if request == "POST":
        form = forms.SnippetForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            body = form.cleaned_data["body"]
            print(name, body)

    form = forms.SnippetForm()
    return render(
        request=request,
        template_name="snippet/form.html",
        context={"form": form},
    )
