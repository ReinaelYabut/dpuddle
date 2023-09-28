from django.shortcuts import render
from persons.models import Doctor, Patient
from .forms import SignupForm
from django.urls import reverse_lazy



# Create your views here.
def index(request):
    doctors = Doctor.objects.all()
    return render(request, 'persons/doctors.html',
                {'doctors': doctors, 'patients': Patient,}
                  )
def contact(request):
    return render(request, 'core/contact.html'
                  )

def doctor(request, doctors=None):
    doctor = Doctor.objects.all()
    return render(request, 'persons/doctors.html',
                  {'doctors': doctors, 'patients': Patient,}
                  )

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SignupForm()
    return render(request, 'core/signup.html', {'form': form})

