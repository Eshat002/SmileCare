from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product, name='product'),
    path('contact-page/', views.contact_page, name='contact-page'),
    path('contact/', views.contact_form_view, name='contact_form_view'),

]

