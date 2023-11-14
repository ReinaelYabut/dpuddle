
from django.db import models

# Create your models here.


from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
User = get_user_model()


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


    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.TextField(default='')
    time = models.TextField(default='')
    doctor = models.CharField(max_length=100)
    room = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class room_details(models.Model):


    def __str__(self):
        return self.name

class Room(models.Model):
    room_number = models.IntegerField(unique=True)


    image= models.ImageField(upload_to='roompic', blank=True, null=True)

    availability = models.BooleanField(default=True)
    room_type = models.CharField(max_length=50)
    num_beds = models.IntegerField()
    bed_type = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return str(self.room_number)


def clean(self):
    super().clean()
    same_room_number = Room.objects.filter(room_number=self.room_number).exclude(pk=self.pk)
    if same_room_number.exists():

        raise ValidationError("Room with this room number already exists.")

        raise ValidationError("Room with this room number already exists.")

