from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    print('2')
    return HttpResponse('Site OLOLOL')


def test(request):
    return HttpResponse('<h1> HI  </h1>')