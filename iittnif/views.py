from django.shortcuts import render, redirect
import os
from django.conf import settings
from django.http import HttpResponse, Http404

def index(request):
    return render(request, 'index.html')

def irnss(request):
    return render(request, 'irnss/irnss.html')

def aboutirnss(request):
    return render(request, 'irnss/about-irnss.html')

def timelineirnss(request):
    return render(request, 'irnss/timeline-irnss.html')

def ongoingResearchirnss(request):
    return render(request, 'irnss/ongoing-research-irnss.html')

def stationsInstituteWorking(request):
    return render(request, 'irnss/stations-institute-working.html')

def irnssGallery(request):
    return render(request, 'irnss/irnss-gallery.html')

def researchArticles(request,id):
    return render(request, f'irnss/research-articles/{id}.htm')

def data(request):

    media_root = settings.MEDIA_ROOT
    
    files = []
    # Walk through the media folder and get all files and folders
    for root, dirs, filenames in os.walk(media_root):
        for filename in filenames:
            # Get the relative file path to preserve folder structure
            relative_path = os.path.relpath(os.path.join(root, filename), media_root)
            files.append(relative_path)

    return render(request, 'data.html', {'files': files})

def contactUs(request):
    return render(request, 'contact-us.html')

def team(request):
    return render(request, 'team.html')