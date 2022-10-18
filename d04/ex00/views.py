from django.shortcuts import render
from django.http import HttpResponse

def homePageView(request):
    return HttpResponse("Hello, World!")

def ex00View(request):
    return render(request, 'index.html')
