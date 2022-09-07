from django.db import models
from django.utils import timezone


class Company(models.Model):
    company_name = models.CharField(max_length=255)
    opening = models.DecimalField(max_digits=10, decimal_places=2)
    closing = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.DecimalField(max_digits=10, decimal_places=2)
    trading_day = models.CharField(max_length=255)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name