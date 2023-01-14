from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

publications_data = [
    {
        'id': 0,
        'title': 'Название',
        'date': datetime.now(),
        'text': 'я того рот!'
    },
    {
        'id': 1,
        'title': 'Название2',
        'date': datetime.now(),
        'text': 'ахахха того рот!'
    }
]


def index(request):
    return render(request, 'main.html')


def Needs(request):
    return render(request, 'Needs.html')


def Geography(request):
    return render(request, 'Geography.html')


def Skills(request):
    return render(request, 'Skills.html')


def LastVac(request):
    return render(request, 'LastVac.html')


def status(request):
    return HttpResponse('Всем1 привет!')
