from django.urls import path

from . import views


app_label = "contact"


urlpatterns = [path("", views.contact, name="contact-list")]
