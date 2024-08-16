from django.shortcuts import render
from .utils.finder import BusinessFinder, get_location
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    """This is the home page"""

    #defaultLocation = get_location(request)
    
    defaultLocation = 'Japan'

    return render(request, 'home.html', {
        'defaultLocation': defaultLocation,
    })

def results(request):
    """This is the results page"""
    
    #defaultLocation = get_location(digitalOcean_ip(request))

    defaultLocation = 'Japan'

    if request.method == 'POST':
        term_query = request.POST.get('term_search', '')
        place_query = request.POST.get('place_search', '')

    place = place_query if place_query else defaultLocation

    try:
        result = BusinessFinder(term_query, place)
        queried_info = list(zip(result.getName(), result.getLocation(), result.getRating(), result.getImage(), result.getUrl()))


        paginator = Paginator(queried_info, 10)
        page_number = request.GET.get('page')

        try:
            agents = paginator.page(page_number)
        except PageNotAnInteger:
            agents = paginator.page(1)
        except EmptyPage:
            agents = paginator.page(paginator.num_pages)

    except Exception:
        return render(request, 'error.html', {
            'error': result.getError().upper
        })
    else:
        return render(request, 'results.html', {
            'defaultLocation': defaultLocation,
            'term_query': term_query,
            'place_query': place_query,
            'info': agents,
            'noInfo': not result.result['businesses'],
        })