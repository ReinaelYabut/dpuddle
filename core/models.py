from django.db import models

# Create your models here.


class contactform(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    message=models.TextField(default='Default Message')

    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name

class medicinelib(models.Model):
    name = models.CharField(max_length=300)
    image= models.ImageField(upload_to='medicine', blank=True, null=True)
    description = models.TextField()
    side_effects = models.TextField()

    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name

class medicine_detail(models.Model):
    medicine = models.OneToOneField(medicinelib, on_delete=models.CASCADE, related_name='detail')
    additional_info=models.TextField()
    usage_info=models.TextField()

    def __str__(self):
        return self.medicine.name

class appointmentsform(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.TextField(default='')
    time = models.TextField(default='')
    doctor = models.CharField(max_length=100)
    room = models.CharField(max_length=100)

    def __str__(self):
        return self.name
