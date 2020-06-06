from django.contrib import admin
from . models import Rental


class RentalAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'min_price', 'max_price', 'location', 'dealer' )
    list_display_links = ('id', 'title')
    list_filter = ('dealer',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'location', 'max_price', 'min_price', 'capacity', 'dealer')
    list_per_page = 20
# Register your models here.
admin.site.register(Rental, RentalAdmin)
