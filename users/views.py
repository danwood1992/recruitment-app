from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import conf
from django.db.models import Q
from .models import Staff_Profile

def staff_Profiles(request):
   
    
    context = {}
    return render(request, 'profiles.html', context)

def cvUpload(request):

   return render (request, 'upload-cv.html')

# Create your views here.
