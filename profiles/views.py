from django.shortcuts import render, get_object_or_404

from .models import UserProfile

# Create your views here.

def profile(request):
    """ Display the user's profile. """

    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)