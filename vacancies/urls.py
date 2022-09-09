from django.urls import path 
from . import views

urlpatterns = [
   
    
    path('vacancy/<str:pk>/', views.vacancy, name="vacancy"),
   
    path('vacancies/', views.vacancies, name='vacancies'),

]