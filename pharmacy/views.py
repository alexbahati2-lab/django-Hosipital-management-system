from django.shortcuts import render, redirect, get_object_or_404
from .models import Medicine
from .models import Medicine, DispenseRecord
from django.contrib.auth.models import User
from reception.models import Patient  # assuming patients are in reception app
from django.contrib.auth.decorators import login_required
from django.utils import timezone

@login_required
def pharmacy_home(request):
    return render(request, 'pharmacy/pharmacy.html')

@login_required
def medicine_list(request):
    medicines = Medicine.objects.all()
    return render(request, 'pharmacy/medicine_list.html', {'medicines': medicines})

@login_required
def issue_medicine(request):
    medicines = Medicine.objects.all()
    patients = Patient.objects.all()
    
    if request.method == 'POST':
        patient_id = request.POST.get('patient')
        medicine_id = request.POST.get('medicine')
        quantity = int(request.POST.get('quantity'))

        patient = get_object_or_404(Patient, pk=patient_id)
        medicine = get_object_or_404(Medicine, pk=medicine_id)

        if quantity > medicine.quantity:
            # Optional: handle insufficient stock
            return render(request, 'pharmacy/issue_medicine.html', {
                'medicines': medicines,
                'patients': patients,
                'error': 'Insufficient stock!'
            })

        # Deduct from stock
        medicine.quantity -= quantity
        medicine.save()

        # Record the issue (using Sale model as dispense record)
        DispenseRecord.objects.create(
            medicine=medicine,
            quantity=quantity,
            sold_by=request.user,  # user who issued
            date=timezone.now()
        )

        return redirect('dispense-history')

    return render(request, 'pharmacy/issue_medicine.html', {'medicines': medicines, 'patients': patients})

@login_required
def dispense_history(request):
    records =  DispenseRecord.objects.all().order_by('-date')  # latest first
    return render(request, 'pharmacy/dispense_history.html', {'dispense_records': records})
