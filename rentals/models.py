from django.db import models
# import datetime
from datetime import datetime
from dealers.models import Dealer


class Rental(models.Model):
    """Create Rental Model"""
    year_choices = []
    for r in range(2000, (datetime.now().year+1)):
        year_choices.append((r,r))


    type_choice = (
        ('Rental', 'Rental'),
    )

    dealer = models.ForeignKey(Dealer, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255)
    type = models.CharField(choices=type_choice, max_length=20)
    min_price = models.IntegerField()
    max_price = models.IntegerField()
    description = models.TextField(blank=True)
    location = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    year = models.IntegerField(('year'), choices=year_choices, default=2000)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    capacity = models.CharField(max_length=50)
    length = models.CharField(max_length=50)
    horsepower = models.CharField(max_length=255)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
