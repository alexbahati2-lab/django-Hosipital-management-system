from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .models import Patient, Appointment, WaitingList   # ✅ Import WaitingList
from django.contrib.auth.decorators import login_required

@login_required
def reception_dashboard(request):
    return render(request, 'reception_dashboard.html')


def reception_dashboard(request):
    return render(request, "reception/dashboard.html")


def patient_list(request):
    patients = Patient.objects.all().order_by('-date_registered')
    return render(request, "reception/patient_list.html", {"patients": patients})


def send_to_queue(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)

    # Prevent duplicate queue entries
    if WaitingList.objects.filter(patient=patient).exists():
        messages.warning(request, "Patient is already in the queue.")
        return redirect('patient_list')

    WaitingList.objects.create(
        patient=patient,
        added_by=request.user
    )

    messages.success(request, f"{patient.full_name} has been added to the waiting queue.")
    return redirect('patient_list')


def register_patient(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        gender = request.POST.get("gender")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        blood_group = request.POST.get("blood_group")
        date_of_birth = request.POST.get("date_of_birth")
        age_input = request.POST.get("age")

        if not date_of_birth and age_input:
            try:
                age = int(age_input)
                today = date.today()
                date_of_birth = date(today.year - age, today.month, today.day)
            except:
                date_of_birth = None

        Patient.objects.create(
            full_name=full_name,
            gender=gender,
            phone=phone,
            address=address,
            blood_group=blood_group,
            date_of_birth=date_of_birth
        )

        return redirect("reception_dashboard")

    return render(request, "reception/register_patient.html")


@login_required
def schedule_appointment(request, patient_id=None):
    patients = Patient.objects.all()

    if request.method == "POST":
        patient_id = request.POST.get("patient")
        date = request.POST.get("date")
        time = request.POST.get("time")
        reason = request.POST.get("reason")

        Appointment.objects.create(
            patient_id=patient_id,
            date=date,
            time=time,
            reason=reason,
            created_by=request.user
        )

        messages.success(request, "Appointment scheduled successfully!")
        return redirect("schedule_appointment")

    return render(request, "reception/schedule_appointment.html", {"patients": patients})
