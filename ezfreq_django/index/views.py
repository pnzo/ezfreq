from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse('Site OLOLOL')


def test(request):
    return HttpResponse('<h1></h1>')