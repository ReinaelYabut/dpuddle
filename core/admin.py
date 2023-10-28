from django.contrib import admin
from .models import contactform, medicinelib, medicine_detail, appointmentsform, Room, room_details


# Register your models here.
admin.site.register(contactform)

admin.site.register(medicinelib)
admin.site.register(medicine_detail)

admin.site.register(appointmentsform)
admin.site.register(Room)
admin.site.register(room_details)
