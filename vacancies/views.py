from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Vacancy, Tag, Salary

def vacancies(request):

    vacancies = Vacancy.objects.all()
    context = {'vacancies': vacancies}
    return render(request, 'vacancies.html', context)

def vacancy(request, pk):
    vacancyObj = Vacancy.objects.get(id=pk)

    return render(request, 'single-vacancy.html')


# Create your views here.
