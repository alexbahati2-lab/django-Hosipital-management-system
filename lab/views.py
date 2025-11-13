from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import TestRequest, TestResult

def lab_dashboard(request):
    """Main dashboard for lab staff to view and manage test requests."""
    test_requests = TestRequest.objects.all()
    return render(request, 'lab/lab_dashboard.html', {'test_requests': test_requests})
