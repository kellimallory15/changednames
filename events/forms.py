from django import forms
from django.forms import ModelForm
from .models import Package, Booking


# Admin SuperUser Booking Form
class BookingFormAdmin(ModelForm):
    class Meta:
        model = Booking
        fields = ('name', 'booking_date', 'package', 'manager', 'attendees', 'description')
        labels = {
            'name': '',
            'booking_date': 'YYYY-MM-DD HH:MM:SS',
            'package': 'Package',
            'manager': 'Photographer',
            'attendees': 'Attendees',
            'description': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Booking Name'}),
            'booking_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Booking Date'}),
            'package': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Package'}),
            'manager': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Manager'}),
            'attendees': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Attendees'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }


# User Booking Form
class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ('name', 'booking_date', 'package', 'attendees', 'description')
        labels = {
            'name': '',
            'booking_date': 'YYYY-MM-DD HH:MM:SS',
            'package': 'Package',
            'attendees': 'Notes',
            'description': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Booking Name'}),
            'booking_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Booking Date'}),
            'package': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Package'}),
            'attendees': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Notes'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }


# Create a package form
class PackageForm(ModelForm):
    class Meta:
        model = Package
        fields = ('name', 'address', 'zip_code', 'phone', 'web', 'email_address', 'package_image')
        labels = {
            'name': '',
            'address': '',
            'zip_code': '',
            'phone': '',
            'web': '',
            'email_address': '',
            'package_image': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Package Name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip Code'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'web': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Web Address'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }
