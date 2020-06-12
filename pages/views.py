from django.shortcuts import render
from django.http import HttpResponse
from rentals.models import Rental
from dealers.models import Dealer
from rentals.choices import year_choices, state_choices, price_choices

# Create your views here.

def index(request):
    rentals = Rental.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'rentals': rentals,
        'year_choices': year_choices,
        'state_choices': state_choices,
        'price_choices': price_choices
    }
    return render(request, 'pages/index.html', context)


def about(request):
    # Get the dealers
    dealers = Dealer.objects.all().filter(is_seller_of_the_month=True)

    # Check whether he is the Seller of the Month
    context = {
        'dealers': dealers
    }
    return render(request, 'pages/about.html', context)
