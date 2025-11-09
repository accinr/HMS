from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django import forms
from .models import Patient, MedicalRecord
from .forms import PatientForm


# ----------------------------------------------------
# PATIENT LIST
# ----------------------------------------------------
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients/patient_list.html', {'patients': patients})


# ----------------------------------------------------
# PATIENT DETAIL
# ----------------------------------------------------
def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    records = MedicalRecord.objects.filter(patient=patient)

    return render(request, 'patients/patient_detail.html', {
        'patient': patient,
        'records': records
    })


# ----------------------------------------------------
# CREATE PATIENT
# ----------------------------------------------------
def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            p = form.save()
            return redirect('patient_detail', pk=p.id)
    else:
        form = PatientForm()

    return render(request, 'patients/patient_form.html', {'form': form})


# ----------------------------------------------------
# EDIT PATIENT
# ----------------------------------------------------
def patient_edit(request, pk):
    patient = get_object_or_404(Patient, pk=pk)

    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_detail', pk=patient.id)
    else:
        form = PatientForm(instance=patient)

    return render(request, 'patients/patient_edit.html', {
        'form': form,
        'patient': patient
    })


# ----------------------------------------------------
# DELETE PATIENT
# ----------------------------------------------------
def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)

    if request.method == 'POST':
        patient.delete()
        return redirect('patient_list')

    return render(request, 'patients/patient_delete.html', {
        'patient': patient
    })


# ====================================================
#                 MEDICAL RECORDS
# ====================================================

# ------------ MEDICAL RECORD FORM ------------
class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ['diagnosis', 'prescription', 'notes']


# ----------------------------------------------------
# ADD MEDICAL RECORD
# ----------------------------------------------------
def medicalrecord_add(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)

    if request.method == 'POST':
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.patient = patient
            record.save()
            return redirect('patient_detail', pk=patient.id)
    else:
        form = MedicalRecordForm()

    return render(request, 'patients/medicalrecord_form.html', {
        'form': form,
        'patient': patient,
    })


# ----------------------------------------------------
# MEDICAL RECORD LIST
# ----------------------------------------------------
def medicalrecord_list(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    records = MedicalRecord.objects.filter(patient=patient)

    return render(request, 'patients/medicalrecord_list.html', {
        'patient': patient,
        'records': records
    })


# ----------------------------------------------------
# MEDICAL RECORD DETAIL
# ----------------------------------------------------
def medicalrecord_detail(request, pk):
    record = get_object_or_404(MedicalRecord, pk=pk)

    return render(request, 'patients/medicalrecord_detail.html', {
        'record': record
    })
