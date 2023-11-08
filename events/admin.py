from django.contrib import admin
from .models import Package
from .models import Client
from .models import Booking
from django.contrib.auth.models import Group

# admin.site.register(Package, PackageAdmin)
admin.site.register(Client)

# Remove Groups
admin.site.unregister(Group)


# admin.site.register(Booking)

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')
    ordering = ('name',)
    search_fields = ('name', 'address')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    fields = (('name', 'package'), 'booking_date', 'description', 'manager', 'approved')
    list_display = ('name', 'booking_date', 'package')
    list_filter = ('booking_date', 'package')
    ordering = ('booking_date',)
