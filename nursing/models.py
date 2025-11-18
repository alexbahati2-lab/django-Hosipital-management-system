
# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
from reception.models import Patient

User = get_user_model()

class Triage(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    nurse = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="nurse_triage")

    temperature = models.CharField(max_length=10, blank=True, null=True)
    blood_pressure = models.CharField(max_length=20, blank=True, null=True)
    pulse_rate = models.CharField(max_length=10, blank=True, null=True)
    weight = models.CharField(max_length=10, blank=True, null=True)
    symptoms = models.TextField(blank=True, null=True)

    status = models.CharField(
        max_length=20,
        default="awaiting",
        choices=[
            ("awaiting", "Awaiting Triage"),
            ("in_progress", "In Progress"),
            ("done", "Triage Complete"),
            ("sent_to_doctor", "Sent to Doctor"),
        ]
    )

    date_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Triage for {self.patient.full_name}"

    class Meta:
        ordering = ['-date_taken']
