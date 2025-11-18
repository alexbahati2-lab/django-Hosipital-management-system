from django.urls import path
from . import views

urlpatterns = [
    path("", views.nursing_dashboard, name="nursing_dashboard"),
    path("start/<int:patient_id>/", views.start_triage, name="start_triage"),
    path("triage/<int:triage_id>/", views.triage_form, name="triage_form"),
]
