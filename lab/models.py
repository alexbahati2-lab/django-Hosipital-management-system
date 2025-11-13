from django.db import models

# Create your models here.
from django.db import models
from reception.models import Patient
from django.conf import settings


class LabTest(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class TestRequest(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    test = models.ForeignKey(LabTest, on_delete=models.CASCADE)
    requested_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ], default='pending')

    def __str__(self):
        return f"{self.test.name} for {self.patient.name}"


class TestResult(models.Model):
    request = models.OneToOneField(TestRequest, on_delete=models.CASCADE)
    result_text = models.TextField()
    requested_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Result for {self.request.patient.name} - {self.request.test.name}"

