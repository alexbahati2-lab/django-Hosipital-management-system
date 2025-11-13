

# Register your models here.
from django.contrib import admin
from .models import Supplier, Medicine, DispenseRecord

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'supplier')

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact')

@admin.register(DispenseRecord)
class DispenseRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'medicine', 'quantity', 'issued_by', 'date')
