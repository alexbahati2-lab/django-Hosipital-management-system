from django.db import models
from datetime import date
from django.conf import settings
from django.utils import timezone
from django.db import models
from datetime import date




class Patient(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('O+', 'O+'), ('O-', 'O-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
    ]

    patient_id = models.CharField(max_length=15, unique=True, editable=False)
    national_id = models.CharField(max_length=20, blank=True, null=True)

    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    blood_group = models.CharField(max_length=5, choices=BLOOD_GROUP_CHOICES, null=True, blank=True)

    next_of_kin_name = models.CharField(max_length=100, null=True, blank=True)
    next_of_kin_phone = models.CharField(max_length=15, null=True, blank=True)

    medical_history = models.TextField(null=True, blank=True)

    date_registered = models.DateTimeField(auto_now_add=True)

    @property
    def age(self):
        if self.date_of_birth:
            today = date.today()
            return today.year - self.date_of_birth.year - (
                (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
            )
        return None

    def save(self, *args, **kwargs):
        if not self.patient_id:
            last_id = Patient.objects.count() + 1
            self.patient_id = f"HMS-{last_id:04d}"   # Format: HMS-0001
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.patient_id} - {self.full_name}"



class Appointment(models.Model):
    patient = models.ForeignKey("Patient", on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)  # ✅ fixed
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.patient.full_name} - {self.date} {self.time}"
    
class WaitingList(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.patient.full_name} - Waiting"