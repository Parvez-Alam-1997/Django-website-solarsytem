from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'home.html')

def sun(request):
    return render(request, 'sun.html')

def mercury(request):
    return render(request, 'mercury.html')

def venus(request):
    return render(request, 'venus.html')

def earth(request):
    return render(request, 'earth.html')

def mars(request):
    return render(request, 'mars.html')

def jupiter(request):
    return render(request, 'jupiter.html')

def saturn(request):
    return render(request, 'saturn.html')

def uranus(request):
    return render(request, 'uranus.html')

def neptune(request):
    return render(request, 'neptune.html')