from django.shortcuts import render, HttpResponse
from . models import Gallery

# Create your views here.

def home(request):
    return render(request, "index.html")

def galeria(request):
    images = Gallery.objects.all()

    context = {
        'images': images,
    }
    return render(request, 'galeria.html', context)