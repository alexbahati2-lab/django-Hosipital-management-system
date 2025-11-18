from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from reception.models import Patient, WaitingList, Appointment
from .models import Consultation, Prescription, LabRequest
from lab.models import LabResult


# -------------------------------------------------------------------
# 🔒 Helper: Allow only doctors & admins
# -------------------------------------------------------------------
def doctor_only(user):
    return user.is_superuser or getattr(user, "role", "") in ["doctor", "admin"]


# -------------------------------------------------------------------
# ✅ DOCTOR DASHBOARD
#   - Shows patients sent from Nursing
#   - Shows direct appointments for today
#   - Shows recent consultations
# -------------------------------------------------------------------
@login_required
def doctor_dashboard(request):
    if not doctor_only(request.user):
        return redirect("home")

    # 🟩 1. Patients sent from Nursing
    waiting_entries = WaitingList.objects.filter(
        status="sent_to_doctor"
    ).select_related("patient").order_by("-timestamp")

    queue_patients = [entry.patient for entry in waiting_entries]

    # 🟦 2. Direct appointments for today
    today = date.today()
    todays_appointments = Appointment.objects.filter(date=today).select_related("patient")

    # 🟧 3. Recent consultations (by this doctor)
    recent_consultations = Consultation.objects.filter(
        doctor=request.user
    ).order_by("-created_at")[:10]

    context = {
        "queue_patients": queue_patients,
        "todays_appointments": todays_appointments,
        "recent_consultations": recent_consultations,
    }

    return render(request, "doctor/doctor_dashboard.html", context)


# -------------------------------------------------------------------
# ✅ CONSULT PATIENT
# -------------------------------------------------------------------
@login_required
def consult_patient(request, patient_id):
    if not doctor_only(request.user):
        return redirect("home")

    patient = get_object_or_404(Patient, id=patient_id)

    consultations = Consultation.objects.filter(patient=patient)
    lab_results = LabResult.objects.filter(lab_request__patient=patient)

    if request.method == "POST":
        notes = request.POST.get("notes", "")
        diagnosis = request.POST.get("diagnosis", "")
        treatment = request.POST.get("treatment", "")

        # ✔ Save main consultation
        consult = Consultation.objects.create(
            patient=patient,
            doctor=request.user,
            notes=notes,
            diagnosis=diagnosis,
            treatment=treatment
        )

        # ✔ Save prescriptions
        meds = request.POST.getlist("medicine[]")
        dosages = request.POST.getlist("dosage[]")
        durations = request.POST.getlist("duration[]")

        for m, d, du in zip(meds, dosages, durations):
            if m.strip():
                Prescription.objects.create(
                    consultation=consult,
                    patient=patient,
                    medicine_name=m.strip(),
                    dosage=d.strip(),
                    duration=du.strip()
                )

        # ✔ Save lab requests
        tests = request.POST.getlist("lab_test[]")
        for test in tests:
            if test.strip():
                LabRequest.objects.create(
                    consultation=consult,
                    patient=patient,
                    doctor=request.user,
                    test_name=test.strip()
                )

        # ✔ Remove patient from doctor queue if they came via Nursing
        WaitingList.objects.filter(
            patient=patient,
            status="sent_to_doctor"
        ).delete()

        return redirect("doctor_dashboard")

    return render(request, "doctor/consultation_form.html", {
        "patient": patient,
        "consultations": consultations,
        "lab_results": lab_results,
    })


# -------------------------------------------------------------------
# ✅ SAVE CONSULTATION (Quick save page)
# -------------------------------------------------------------------
@login_required
def save_consultation(request, patient_id):
    if not doctor_only(request.user):
        return redirect("home")

    patient = get_object_or_404(Patient, id=patient_id)

    if request.method == "POST":
        Consultation.objects.create(
            patient=patient,
            doctor=request.user,
            notes=request.POST.get("notes", ""),
            diagnosis=request.POST.get("diagnosis", ""),
            treatment=request.POST.get("treatment", "")
        )
        return redirect("consult_patient", patient_id=patient.id)

    return render(request, "doctor/save_consultation.html", {"patient": patient})


# -------------------------------------------------------------------
# ✅ PATIENT HISTORY PAGE
# -------------------------------------------------------------------
@login_required
def patient_history(request, patient_id):
    if not doctor_only(request.user):
        return redirect("home")

    patient = get_object_or_404(Patient, id=patient_id)
    consultations = Consultation.objects.filter(patient=patient)

    return render(request, "doctor/patient_history.html", {
        "patient": patient,
        "consultations": consultations
    })
