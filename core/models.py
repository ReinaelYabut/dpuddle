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
