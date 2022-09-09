from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.models import Staff_Profile

def getHome(request):
   
   return render (request,'home.html')

def getAbout(request):

   return render (request, 'about.html')

def getFaq(request):

   return render (request, 'faq.html')

def getContact(request):

   return render (request, 'contact.html')

   




# Create your views here.
