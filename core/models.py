from django.db import models

# Create your models here.


class contactform(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    message=models.TextField(default='Default Message')