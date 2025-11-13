from django.urls import path
from . import views

urlpatterns = [
    path('', views.reception_dashboard, name='reception_dashboard'),
    path('register-patient/', views.register_patient, name='register_patient'),
    path('patients/', views.patient_list, name='patient_list'),
    path('schedule-appointment/', views.schedule_appointment, name='schedule_appointment'),
    path('send-to-queue/<int:patient_id>/', views.send_to_queue, name='send_to_queue'),
]
