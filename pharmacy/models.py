from django.db import models
from django.conf import settings

from reception.models import Patient  # your patient model

class Medicine(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    quantity = models.PositiveIntegerField(default=0)
    supplier = models.CharField(max_length=255, blank=True)

class DispenseRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    issued_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    date = models.DateTimeField(auto_now_add=True)

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

