# Generated by Django 4.2.4 on 2023-10-26 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_remove_medicinelib_form_medicinelib_form'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='medicinelib',
            name='form',
        ),
        migrations.DeleteModel(
            name='dosageform',
        ),
        migrations.AddField(
            model_name='medicinelib',
            name='categories',
            field=models.ManyToManyField(to='core.category'),
        ),
    ]
