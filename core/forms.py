from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from persons.models import Doctor


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1','password2')

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'specialty', 'phone', 'email', 'address', 'image', ]
