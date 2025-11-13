from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Invoice

def billing_dashboard(request):
    invoices = Invoice.objects.all().order_by('-date_issued')
    return render(request, 'billing/billing_dashboard.html', {'invoices': invoices})
