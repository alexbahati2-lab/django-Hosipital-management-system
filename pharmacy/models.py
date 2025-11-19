from django.db import models
from django.conf import settings
from reception.models import Patient  # Your patient model


class Supplier(models.Model):
    """Suppliers providing medicines."""
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Medicine(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    quantity = models.PositiveIntegerField(default=0)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # selling price

    def __str__(self):
        return self.name

class Prescription(models.Model):
    """Prescriptions issued to patients."""
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medicine = models.CharField(max_length=255)  # or link to Medicine if desired
    instructions = models.TextField(blank=True)
    issued_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.name} prescription"


class DispenseRecord(models.Model):
    """Records of medicines dispensed to patients."""
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    issued_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.medicine.name} to {self.patient.name} on {self.date.strftime('%Y-%m-%d')}"
