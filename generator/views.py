from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(reguest):
    return render(reguest, 'generator/home.html')
def password(reguest):
    return render(reguest, 'generator/password.html')