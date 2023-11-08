import datetime

import stripe as stripe
from django.shortcuts import render
from django.views import generic
from photologue.models import Gallery
from photologue.views import GalleryListView, PhotoDetailView

from .forms import OrderForm
from .models import PhotographySession, Booking
from django.conf import settings
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


class CustomGalleryListView(GalleryListView):
    template_name = 'photologue/gallery_list.html'

    def get_queryset(self):
        return Gallery.objects.filter(title__icontains='')


class CustomPhotoDetailView(PhotoDetailView):
    template_name = 'photologue/photo_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def index(request):
    context = {

    }

    return render(request, 'index.html', context=context)


def about(request):
    return render(request, 'about.html')


def senior_about(request):
    return render(request, 'senior_about.html')


def family_about(request):
    return render(request, 'family_about.html')


def couples_engagements_about(request):
    return render(request, 'couples_engagements_about.html')


def calendar(request):
    return render(request, 'calendar.html')


class CalendarView(generic.DetailView):
    model = Booking


def view_cart(request):
    cart = request.session.get('cart', [])  # Get the cart from the session
    sessions_in_cart = PhotographySession.objects.filter(id__in=cart)

    return render(request, 'shopping_cart.html', {'sessions_in_cart': sessions_in_cart})


stripe.api_key = settings.STRIPE_SECRET_KEY


def create_booking(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            product_name = form.cleaned_data['product_name']
            amount = form.cleaned_data['amount'] * 100  # Convert to cents

            # Create a Stripe PaymentIntent
            payment_intent = stripe.PaymentIntent.create(
                amount=int(amount),
                currency='usd',
                description=product_name
            )

            return render(request, 'payment.html', {'client_secret': payment_intent.client_secret})

    else:
        form = OrderForm()

    return render(request, 'order_information_input.html', {'form': form})


def calendar_view(request):
    month = request.GET.get('month', None)
    year = request.GET.get('year', None)

    if month and year:
        currentDate = datetime.date(int(year), int(month), 1)
    else:
        currentDate = datetime.date.today()

    bookings_for_month = Booking.objects.filter(date__month=currentDate.month, date__year=currentDate.year)

    booked_dates = [b.date.day for b in bookings_for_month]

    return render(request, 'calendar.html', {'booked_dates': booked_dates, 'current_month': currentDate.month,
                                             'current_year': currentDate.year})

    # return JsonResponse({
    #     'booked_dates': booked_dates,
    #     'current_month': currentDate.month,
    #     'current_year': currentDate.year
    # })
