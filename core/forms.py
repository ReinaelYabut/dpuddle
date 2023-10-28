from django import forms
from django.contrib.auth.forms import UserCreationForm
#changed import from defaul user model to customer user model
from authuser.models import User

from persons.models import Doctor


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1','password2')


class CreateUserForm(UserCreationForm):#changed from UserCreationForm to ModelForm
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        "class": "form-control",
    }))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={
        "class": "form-control",
    }))
    class Meta:
        model = User
        fields = ['email', 'password1']

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'specialty', 'phone', 'email', 'address', 'image', ]
