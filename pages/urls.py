from django.urls import path 
from . import views

urlpatterns = [


path('', views.getHome, name="home"),
path('about', views.getAbout, name="about"),
path('faq', views.getFaq, name="faq"),
path('contact', views.getContact, name="contact")
]