from django.shortcuts import render
from persons.models import Doctor, Patient



# Create your views here.
def index(request):
    persons = Doctor.objects.all()
    return render(request, 'core/index.html',
                {'doctors': Doctor, 'patients': Patient,}
                  )
def contact(request):
    return render(request, 'core/contact.html'
                  )
