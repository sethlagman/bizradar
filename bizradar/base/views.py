from django.shortcuts import render
from utils.finder import BusinessFinder, get_location

def home(request):
    """This is the home page"""

    defaultLocation = get_location(digitalOcean_ip(request))
    
    #defaultLocation = 'Japan'

    return render(request, 'home.html', {
        'defaultLocation': defaultLocation,
    })