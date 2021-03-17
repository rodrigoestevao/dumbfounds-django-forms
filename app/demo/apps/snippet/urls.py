from django.urls import path

from . import views


app_label = "snippet"


urlpatterns = [path("", views.snippet, name="snippet-list")]
