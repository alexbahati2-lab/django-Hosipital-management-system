from django.db import models
from django.contrib.auth import get_user_model
from reception.models import Patient

User = get_user_model()

STATUS_CHOICES = [
    ('waiting', 'Waiting'),
    ('in_progress', 'In Progress'),
    ('completed', 'Completed'),
]



class Consultation(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="consultations"
    )
    doctor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="doctor_consultations"
    )
    notes = models.TextField(blank=True, null=True)
    diagnosis = models.TextField(blank=True, null=True)
    treatment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='waiting')

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Consultation"
        verbose_name_plural = "Consultations"

    def __str__(self):
        return f"Consultation: {self.patient.full_name} ({self.created_at.strftime('%Y-%m-%d')})"


class Prescription(models.Model):
    consultation = models.ForeignKey(
        Consultation,
        on_delete=models.CASCADE,
        related_name="doctor_prescriptions"
    )
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="doctor_prescriptions_patient"
    )
    medicine_name = models.CharField(max_length=255)
    dosage = models.CharField(max_length=255, blank=True, null=True)
    duration = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.medicine_name} for {self.patient.full_name}"


class LabRequest(models.Model):
    consultation = models.ForeignKey(
        Consultation,
        on_delete=models.CASCADE,
        related_name="doctor_lab_requests",
        null=True,
        blank=True
    )
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="doctor_lab_requests_patient"
    )
    doctor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="doctor_sent_lab_requests"
    )
    test_name = models.CharField(max_length=255)
    status = models.CharField(max_length=50, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Lab Test: {self.test_name} for {self.patient.full_name}"
