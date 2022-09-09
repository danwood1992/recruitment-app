from django.urls import path 
from . import views

urlpatterns = [


path('profiles/', views.staff_Profiles, name="profiles"),
path('upload-cv/', views.cvUpload, name='upload-cv'),
]