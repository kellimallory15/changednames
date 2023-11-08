from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
BOOKING_OPTIONS = (
    ("Senior Portrait Package", "Senior Portrait Package"),
    ("Couples & Engagements Package", "Couples & Engagements Package"),
    ("Family Package", "Family Package"),
)
TIME_OPTIONS = (
    ("3 PM", "3 PM"),
    ("3:30 PM", "3:30 PM"),
    ("4 PM", "4 PM"),
    ("4:30 PM", "4:30 PM"),
    ("5 PM", "5 PM"),
    ("5:30 PM", "5:30 PM"),
    ("6 PM", "6 PM"),
    ("6:30 PM", "6:30 PM"),
    ("7 PM", "7 PM"),
    ("7:30 PM", "7:30 PM"),
)


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    service = models.CharField(max_length=50, choices=BOOKING_OPTIONS, default="Senior Portrait Package")
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_OPTIONS, default="3 PM")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.user.username} | day: {self.day} | time: {self.time}"
