from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def aboutme(request):
    return render(request, 'aboutme.html')
