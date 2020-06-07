from django.shortcuts import render
from django.http import HttpResponse
from rentals.models import Rental

# Create your views here.

def index(request):
    rentals = Rental.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'rentals': rentals,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')
