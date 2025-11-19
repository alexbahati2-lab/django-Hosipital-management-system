from django.urls import path
from . import views

urlpatterns = [
    path('', views.pharmacy_home, name='pharmacy-home'),
    path('medicines/', views.medicine_list, name='medicine-list'),
    path('issue/', views.issue_medicine, name='issue-medicine'),
    path('history/', views.dispense_history, name='dispense-history'),
    path('add/', views.add_medicine, name='add-medicine'),  # <-- make sure this exists
]
