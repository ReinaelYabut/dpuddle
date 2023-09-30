from django.shortcuts import render, redirect

from persons.decorators import unaunthenticated_user
from persons.models import Doctor, Patient
from .forms import CreateUserForm, DoctorForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from authuser.models import User

from django.contrib.auth.decorators import login_required
from persons.decorators import unaunthenticated_user


# Create your views here.
@login_required(login_url='core:login')
def index(request):
    doctors = Doctor.objects.all()
    return render(request, 'core/home.html',
              {'doctors': doctors, 'patients': Patient,}
                  )


@login_required(login_url='core:login')
def contact(request):
    return render(request, 'core/contact.html'
                  )


@login_required(login_url='core:login')
def doctor(request, doctors=None):
    doctors = Doctor.objects.all()

    return render(request, 'persons/doctors.html',
                  {'doctors': doctors, 'patients': Patient, }
                  )


@unaunthenticated_user
def registerPage(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + form.cleaned_data.get('username'))

            return redirect('core:login')
    context = {'form': form}
    return render(request, 'core/register.html', context)



@unaunthenticated_user
def loginPage(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            print('asd')
            login(request, user)
            return redirect('core:index')
        else:
            messages.info(request, 'Username or Password is incorrect')
    context = {}
    return render(request, 'core/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('core:login')


def userPage(request):
    context = {}
    return render(request, 'core/user.html', context)


def home(request):
    return render(request, 'core/home.html')


@login_required(login_url='core:login')
def about(request):
    return render(request, 'core/about.html')


def privacypolicy(request):
    return render(request, 'core/privacypolicy.html')

class DoctorCreateView(CreateView):
    form_class = DoctorForm
    template_name = 'core/doctors/create_view.html'
    success_url = reverse_lazy('core:doctor')



