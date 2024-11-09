from django.shortcuts import render, HttpResponse
from . models import Gallery
from . models import Gallery_home

# Create your views here.

def home(request):
    img = Gallery_home.objects.all()

    context = {
        'img': img,
    }
    return render(request, "index.html", context)

#def galeria(request):
#    return render(request, "galeria.html")

def galeria(request):
    images = Gallery.objects.all()

    context = {
        'images': images,
    }
    return render(request, 'galeria.html', context)

def sobre(request):
    return render(request, "sobre.html")