from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(reguest):
    return render(reguest, 'generator/home.html')
def password(reguest):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if reguest.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if reguest.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+'))
    if reguest.GET.get('numbers'):
        characters.extend(list('0123456789'))
    lenght = int(reguest.GET.get('lenght', 12))

    thepassword = ''
    for x in range(lenght):
        thepassword += random.choice(characters)
    return render(reguest, 'generator/password.html', {'password':thepassword})