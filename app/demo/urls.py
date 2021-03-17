from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("contact/", include("demo.apps.contact.urls")),
    path("snippet/", include("demo.apps.snippet.urls")),
]
