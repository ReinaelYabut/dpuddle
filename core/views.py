from django.db.models import Q
from django.http import HttpResponseForbidden
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

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from django.contrib.auth.decorators import login_required
from persons.decorators import unaunthenticated_user

from .models import contactform, medicinelib, medicine_detail, appointmentsform, Room, room_details


# Create your views here.
@login_required(login_url='core:login')
def index(request):
    doctors = Doctor.objects.all()
    return render(request, 'core/home.html',
              {'doctors': doctors, 'patients': Patient,}
                  )


@login_required(login_url='core:login')
def contact(request):
    if request.method=="POST":
        post=contactform()
        post.name=request.POST['name']
        post.email=request.POST['email']
        post.message=request.POST['message']

        post.save()
        return render(request, 'core/contact.html')
    else:
        return render(request, 'core/contact.html')



@login_required(login_url='core:login')
def doctor(request, doctors=None):
    # if not request.user.is_superuser:
    #     # Handle the case where the user is not a superuser
    #     return HttpResponseForbidden("You do not have permission to access this page.")

    doctors = Doctor.objects.all()

    return render(request, 'persons/doctors.html',
                  {'doctors': doctors, 'patients': Patient.objects.all()})
# added this new function for doctor detail
@login_required(login_url='core:login')
def doctorDetails(request, pk):
    doctors = Doctor.objects.get(id=pk)
    print(doctors)
    return render(request, 'persons/doctor_detail.html',
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
            # Changed username to email
            messages.success(request, 'Account was created for ' + form.cleaned_data.get('email'))

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

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseForbidden("You do not have permission to access this page.")
        return super().dispatch(request, *args, **kwargs)
def medicines(request):
    medicine = medicinelib.objects.all()
    
    page = request.GET.get('page')
    paginator = Paginator(medicine, 3)
    try:
        medicine = paginator.page(page)
    except PageNotAnInteger:
        medicine = paginator.page(1)
    except EmptyPage:
        medicine = paginator.page(paginator.num_pages)

    
    return render(request, 'core/medicines.html', {'medicine': medicine})


def medfilterview(request):
    medicine_contains_query = request.GET.get('medicine_contains')

    if medicine_contains_query and medicine_contains_query.strip():
        queryset = medicinelib.objects.filter(name__icontains=medicine_contains_query)
    else:
        queryset = medicinelib.objects.all()

    context = {
        'queryset': queryset,
        'medicine_contains_query': medicine_contains_query,
    }

    return render(request, 'core/medicines.html', context)


def medicinedetail(request, med_id):
    medicine = medicinelib.objects.get(pk=med_id)
    detail = medicine.detail
    return render(request, 'core/medicinedetail.html', {'medicine': medicine, 'detail': detail})


def room_list(request):
    # rooms.object
    room = Room.objects.all()
    print(room)
    context = {
        'room': room
    }
    return render(request, 'core/rooms.html', context)

# def appointments(request):
#     return render(request, 'core/appointments.html')

def room_details(request, room_id):
    room = Room.objects.get(pk=room_id)
    print(room)
    return render(request, 'core/room_details.html', {'room': room})

@login_required(login_url='core:login')
def patients(request):
    patients_data = Patient.objects.all()
    appointments_data = appointmentsform.objects.all()
    return render(request, 'core/patients.html',
                  {'patients_data': patients_data, 'appointments_data': appointments_data})
    if not request.user.is_superuser:
        return HttpResponseForbidden("You do not have permission to access this page.")

    return render(request, 'core/patients.html')

def appointments(request):
    queryset = Doctor.objects.all()
    print(queryset)
    Queryset = Room.objects.all()
    print(Queryset)
    if request.method=="POST":
        print(request.POST)
        print(request.POST['room'])
        post=appointmentsform()
        room_obj = Room.objects.get(room_number=request.POST['room'])
        print(room_obj.availability)

        post.user = request.user
        post.name = request.POST['name']
        post.phone = request.POST['phone']
        post.email = request.POST['email']
        post.date = request.POST['date']
        post.time = request.POST['time']
        post.doctor = request.POST['doctor']
        post.room = request.POST['room']
        if room_obj.availability is True:
            room_obj.availability = False
            room_obj.save()
        post.save()
        return render(request, 'core/appointments.html', {'query': queryset, 'Query' : Queryset})
    else:
        return render(request, 'core/appointments.html', {'query': queryset, 'Query' : Queryset})
def docfilterview(request):
    doctor_contains_query = request.GET.get('doctor_contains')
    print(doctor_contains_query)
    if doctor_contains_query and doctor_contains_query.strip():
        queryset = Doctor.objects.filter(name__icontains=doctor_contains_query)
    else:
        queryset = Doctor.objects.all()

    context = {
        'queryset': queryset,
        'doctor_contains_query': doctor_contains_query,
    }

    return render(request, 'persons/doctors.html', context)
