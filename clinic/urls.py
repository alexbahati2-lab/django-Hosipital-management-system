from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctor_dashboard, name='doctor_dashboard'),  # Clinic home (Doctor dashboard)
    path('consult/<int:patient_id>/', views.consult_patient, name='consult_patient'),
]
