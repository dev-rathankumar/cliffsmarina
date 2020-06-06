from django.db import models
from datetime import datetime
# Create your models here.


class Dealer(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    dob = models.DateField(max_length=8)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=100)
    description = models.TextField(max_length=255, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)
    is_sellet_of_the_month = models.BooleanField(default=False)
    registered_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
