from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.home, name="home"),
    path("contact/", views.contact_form_view, name="contact_form_view"),
    path("articles/", views.articles, name="articles"),
]
