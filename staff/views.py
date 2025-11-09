# staff/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from .models import Doctor


# ----------------------------------------------------
# DOCTOR FORM (used for create & edit)
# ----------------------------------------------------
class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name', 'specialization', 'phone', 'email', 'available']


# ----------------------------------------------------
# DOCTOR LIST
# ----------------------------------------------------
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'staff/doctor_list.html', {'doctors': doctors})


# ----------------------------------------------------
# DOCTOR DETAIL
# ----------------------------------------------------
def doctor_detail(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    return render(request, 'staff/doctor_detail.html', {'doctor': doctor})


# ----------------------------------------------------
# CREATE DOCTOR
# ----------------------------------------------------
def doctor_create(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            doctor = form.save()
            return redirect('doctor_detail', pk=doctor.id)
    else:
        form = DoctorForm()

    return render(request, 'staff/doctor_form.html', {'form': form})


# ----------------------------------------------------
# EDIT DOCTOR
# ----------------------------------------------------
def doctor_edit(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)

    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor_detail', pk=doctor.id)
    else:
        form = DoctorForm(instance=doctor)

    return render(request, 'staff/doctor_edit.html', {
        'form': form,
        'doctor': doctor
    })


# ----------------------------------------------------
# DELETE DOCTOR
# ----------------------------------------------------
def doctor_delete(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)

    if request.method == 'POST':
        doctor.delete()
        return redirect('doctor_list')

    return render(request, 'staff/doctor_delete.html', {
        'doctor': doctor
    })
