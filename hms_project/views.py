from django.shortcuts import render
from patients.models import Patient
from staff.models import Doctor
from appointments.models import Appointment

def dashboard(request):
    return render(request, 'dashboard.html', {
        'patients': Patient.objects.count(),
        'doctors': Doctor.objects.count(),
        'appointments': Appointment.objects.count(),
    })
