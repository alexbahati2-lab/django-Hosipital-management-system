from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from reception.models import Patient
from .models import Consultation

@login_required
def doctor_dashboard(request):
    # Allow only: doctor, admin, or superuser
    if not (request.user.is_superuser or request.user.role in ["doctor", "admin"]):
        return redirect('home')  # send others back to home

    patients = Patient.objects.filter(waitinglist=True).order_by('-date_registered')
    return render(request, 'clinic/doctor_dashboard.html', {'patients': patients})


@login_required
def consult_patient(request, patient_id):
    # Same access restriction here
    if not (request.user.is_superuser or request.user.role in ["doctor", "admin"]):
        return redirect('home')

    patient = get_object_or_404(Patient, id=patient_id)

    if request.method == 'POST':
        notes = request.POST.get('notes')
        diagnosis = request.POST.get('diagnosis')
        treatment = request.POST.get('treatment')

        Consultation.objects.create(
            patient=patient,
            notes=notes,
            diagnosis=diagnosis,
            treatment=treatment
        )

        patient.waitinglist = False
        patient.save()

        return redirect('doctor_dashboard')

    return render(request, 'clinic/consultation_form.html', {'patient': patient})
