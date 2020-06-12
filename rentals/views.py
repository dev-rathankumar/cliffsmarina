from django.shortcuts import render, get_object_or_404
from . models import Rental
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from . models import Dealer
from rentals.choices import year_choices, state_choices, price_choices
# Create your views here.


def index(request):
    rentals = Rental.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(rentals, 6)
    page = request.GET.get('page')
    paged_rentals = paginator.get_page(page)
    context = {
        'rentals': paged_rentals
    }
    return render(request, 'rentals/rentals.html', context)


def rental(request, rental_id):
    single_rental = get_object_or_404(Rental, pk=rental_id)

    context = {
        'single_rental': single_rental
    }
    return render(request, 'rentals/rental.html', context)


def search(request):
    # Get all the listings by date
    queryset_list = Rental.objects.order_by('-list_date')

    # keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(location__iexact=state)

    # Years
    if 'years' in request.GET:
        years = request.GET['years']
        if years:
            queryset_list = queryset_list.filter(year__iexact=years)

    # price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(min_price__lte=price)


    context = {
        'year_choices' : year_choices,
        'state_choices' : state_choices,
        'price_choices' : price_choices,
        'rentals': queryset_list,
        'values' : request.GET
    }
    return render(request, 'rentals/search.html', context)
