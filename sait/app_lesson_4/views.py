from django.shortcuts import render
from django.http import HttpResponse

# def index(request):
#     return HttpResponse('Домашка по 4 занятию')

# Create your views here.
def index(request):
    return render(request, 'index.html')

def go_back(request):
    return render (request, 'go back.html')

