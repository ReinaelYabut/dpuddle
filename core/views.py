from django.shortcuts import render, redirect
from persons.models import Doctor, Patient
from .forms import CreateUserForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


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

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,'Account was created for ' + form.cleaned_data.get('username'))

            return redirect('core:login')

    context = { 'form': form }
    return render(request, 'core/register.html', context)

def loginPage(request, context=None):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, username)
            redirect('core:home')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'core/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('core:login')


def home(request):
    return render(request, 'core/home.html')