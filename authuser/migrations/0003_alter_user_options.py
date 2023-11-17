# Generated by Django 4.2.4 on 2023-11-17 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authuser', '0002_user_is_staff'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [('view_all_sites', 'Can view all sites'), ('view_patient_sites', 'Can view patient-specific sites')], 'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
    ]
