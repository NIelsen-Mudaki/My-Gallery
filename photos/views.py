from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import *

# Create your views here.
def home(request):
    images = Image.objects.all()
    return render(request,'home.html', {'images':images})


def search_results(request):
    
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_photos = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-photo/search.html',{"message":message,"photos": searched_photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photo/search.html',{"message":message})