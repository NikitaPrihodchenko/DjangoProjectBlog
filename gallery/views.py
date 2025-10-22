from django.shortcuts import render
from .models import GalleryImage


def gallery(request):
    images = GalleryImage.objects.all()
    return render(request, "gallery/index.html", {'images': images})


def upload(request):
    return render(request, "gallery/upload.html")
