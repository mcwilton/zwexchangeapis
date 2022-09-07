from django.db import models
from django.utils import timezone


class Company(models.Model):
    company_name = models.CharField(max_length=255, default="")
    opening = models.DecimalField(max_digits=10, decimal_places=2, default="")
    closing = models.DecimalField(max_digits=10, decimal_places=2, default="")
    volume = models.IntegerField(blank=False, default="")
    trading_day = models.CharField(max_length=255, default='00/00/0000')
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name