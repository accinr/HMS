# appointments/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Appointment
from .forms import AppointmentForm


# ----------------------------------------------------
# APPOINTMENT LIST
# ----------------------------------------------------
def appointment_list(request):
    appts = Appointment.objects.select_related('patient', 'doctor').all()
    return render(request, 'appointments/appointment_list.html', {'appts': appts})


# ----------------------------------------------------
# APPOINTMENT DETAIL
# ----------------------------------------------------
def appointment_detail(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    return render(request, 'appointments/appointment_detail.html', {'appointment': appointment})


# ----------------------------------------------------
# CREATE APPOINTMENT
# ----------------------------------------------------
def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()

    return render(request, 'appointments/appointment_form.html', {'form': form})


# ----------------------------------------------------
# EDIT APPOINTMENT
# ----------------------------------------------------
def appointment_edit(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)

    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment_detail', pk=appointment.id)
    else:
        form = AppointmentForm(instance=appointment)

    return render(request, 'appointments/appointment_edit.html', {
        'form': form,
        'appointment': appointment
    })


# ----------------------------------------------------
# DELETE APPOINTMENT
# ----------------------------------------------------
def appointment_delete(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)

    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment_list')

    return render(request, 'appointments/appointment_delete.html', {
        'appointment': appointment
    })
