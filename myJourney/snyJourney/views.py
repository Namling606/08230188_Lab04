from django.shortcuts import render

# Create your views here.
from .models import LearningJourney, AboutMe

def index(request):
    # fetch all journey entries
    journeys = LearningJourney.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'journeys': journeys})

def about_me(request):
    # get first AboutMe entry (or none)
    about = AboutMe.objects.first()
    return render(request, 'aboutMe.html', {'about': about})
