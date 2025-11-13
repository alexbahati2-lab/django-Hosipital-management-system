from django.db import models

# Create your models here.
from django.db import models
from reception.models import Patient   # <-- Import Patient model

class Consultation(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    notes = models.TextField()
    diagnosis = models.TextField()
    treatment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Consultation for {self.patient.full_name} on {self.date.strftime('%Y-%m-%d')}"
