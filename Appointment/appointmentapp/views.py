from django.shortcuts import render
from appointmentapp.models import *
from appointmentapp.serializers import *
from rest_framework.viewsets import *
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.exceptions import ValidationError
# from django_filters.rest_framework import DjangoFilterBackend


class DoctorView(ModelViewSet):
	queryset=Doctor.objects.all()
	serializer_class=DoctorSerializer

class PatientView(ModelViewSet):
	queryset=Patient.objects.all()
	serializer_class=PatientSerializer

class AppointmentView(ModelViewSet):
	queryset=Appointment.objects.all()
	serializer_class=AppointmentSerializer

	def perform_create(self, serializer):
		print(self.request.data)
		doc=self.request.data['Doctor_field']
		pat=self.request.data['Patient_field']
		date=self.request.data['date']

		queryset = Appointment.objects.filter(Doctor_field=doc,Patient_field=pat,date=date)
		if queryset.exists():
			raise ValidationError('You have already signed up')
		serializer.save()

		
	
	

	# def get_queryset(self):
	# 	queryset = Patient.objects.all()
	# 	Patient_name = self.request.query_params.get('Patient_name',None)
	# 	doctor_num =self.request.query_params.get('Patient_name',None)
	# 	if Patient_name is not None:
	# 		queryset = queryset.filter(Patient_name=Patient_name)
	# 	return queryset

		





