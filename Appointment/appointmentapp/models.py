from django.db import models

class Doctor(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Patient(models.Model):
	doctor_num = models.ForeignKey(Doctor,on_delete=models.CASCADE)
	Patient_name = models.CharField(max_length=50)
	age = models.IntegerField()
	Gender = models.CharField(max_length=50)
	contact_num= models.IntegerField()
	Appointment_date = models.DateField()
	
	def __str__(self):
		return self.Patient_name

class Appointment(models.Model):
	Doctor_field=models.ForeignKey(Doctor,on_delete=models.CASCADE)
	Patient_field=models.ForeignKey(Patient,on_delete=models.CASCADE)
	date = models.DateField()






