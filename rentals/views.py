from django.shortcuts import render
from . models import Rental
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
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
    return render(request, 'rentals/rental.html')


def search(request):
    return render(request, 'rentals/search.html')
