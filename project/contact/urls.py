from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.contact_info,name="contact_info"),
]
