# Generated by Django 3.1 on 2021-03-05 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointmentapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('Doctor_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointmentapp.doctor')),
                ('Patient_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointmentapp.patient')),
            ],
        ),
    ]
