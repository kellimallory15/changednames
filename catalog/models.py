from django.db import models
from django.urls import reverse
from django import forms


class PhotographySession(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Client(models.Model):
    client_id = models.CharField(max_length=200, primary_key=True)
    f_name = models.CharField(max_length=200)
    l_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.fname} {self.lname}'


class Package(models.Model):
    package_id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    duration = models.DateField()

    def __str__(self):
        return self.name


class Booking(models.Model):
    BOOKING_STATUS_CHOICES = [
        ('Approved', 'Approved'),
        ('Needs Rescheduled', 'Needs Rescheduled'),
        ('Pending Approval', 'Pending Approval')
    ]

    booking_id = models.CharField(max_length=200, primary_key=True)
    booking_datetime = models.DateTimeField()
    status = models.CharField(max_length=20, choices=BOOKING_STATUS_CHOICES, default='Pending Approval')
    created_date = models.DateTimeField()
    last_updated = models.DateTimeField()
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.booking_id

    def get_absolute_url(self):
        return reverse('calendar', args=[str(self.id)])


class Photo(models.Model):
    photo_id = models.CharField(max_length=200, primary_key=True)
    file_path = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    package = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='photos')

    def __str__(self):
        return self.photo_id
