from django.urls import path
from . import views

urlpatterns = [
    # Doctor dashboard
    path('', views.doctor_dashboard, name='doctor_dashboard'),

    # Consult patient (main page)
    path('consult/<int:patient_id>/', views.consult_patient, name='consult_patient'),

    # Save consultation only
    path('consult/<int:patient_id>/save/', views.save_consultation, name='save_consultation'),

    # Patient consultation history
    path('history/<int:patient_id>/', views.patient_history, name='patient_history'),
]
