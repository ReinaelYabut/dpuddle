from django.db import models

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=50)
    specialty = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    image = models.ImageField(upload_to='doctors', blank=True, null=True)

    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name


class Appointment(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name

