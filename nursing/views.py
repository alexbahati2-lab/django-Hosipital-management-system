from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from reception.models import WaitingList, Patient
from .models import Triage
from doctor.models import Consultation  # import Consultation

@login_required
def nursing_dashboard(request):
    # patients waiting from reception
    waiting_patients = WaitingList.objects.all().order_by("-added_at")  # corrected field name

    # patients currently being triaged
    triaging = Triage.objects.filter(status="in_progress").order_by("-date_taken")

    # patients recently sent to doctor
    recently_sent = Triage.objects.filter(status="sent_to_doctor").order_by("-date_taken")[:10]

    return render(request, "nursing/dashboard.html", {
        "waiting_patients": waiting_patients,
        "triaging": triaging,
        "recently_sent": recently_sent,
    })


@login_required
def start_triage(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)

    # Remove from reception queue
    WaitingList.objects.filter(patient=patient).delete()

    triage = Triage.objects.create(
        patient=patient,
        nurse=request.user,
        status="in_progress"
    )

    return redirect("triage_form", triage.id)


@login_required
def triage_form(request, triage_id):
    triage = get_object_or_404(Triage, id=triage_id)

    if request.method == "POST":
        triage.temperature = request.POST.get("temperature")
        triage.blood_pressure = request.POST.get("blood_pressure")
        triage.pulse_rate = request.POST.get("pulse_rate")
        triage.weight = request.POST.get("weight")
        triage.symptoms = request.POST.get("symptoms")
        triage.status = "sent_to_doctor"
        triage.save()

        # Create an empty Consultation for doctor
        # Here you can optionally assign a default doctor or leave None
        Consultation.objects.create(
            patient=triage.patient,
            doctor=None,  # you can assign a doctor later
            notes='',
            diagnosis='',
            treatment=''
        )

        messages.success(request, "Triage completed and patient sent to doctor.")
        return redirect("nursing_dashboard")

    return render(request, "nursing/triage_form.html", {"triage": triage})
