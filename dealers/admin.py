from django.contrib import admin
from . models import Dealer

class DealerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'city', 'is_seller_of_the_month', 'registered_date' )
    list_editable = ('is_seller_of_the_month',)
    list_filter = ('city',)
    list_per_page = 20
    list_display_links = ('name',)
    search_fields = ('name', 'email', 'id', 'phone', 'city', 'state', 'zipcode')
# Register your models here.
admin.site.register(Dealer, DealerAdmin)
