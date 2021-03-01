from django.shortcuts import render
from appointmentapp.models import *
from appointmentapp.serializers import *
from rest_framework.viewsets import *
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# from django_filters.rest_framework import DjangoFilterBackend


class DoctorView(ModelViewSet):
	queryset=Doctor.objects.all()
	serializer_class=DoctorSerializer

class PatientView(ModelViewSet):
	queryset=Patient.objects.all()
	serializer_class=PatientSerializer
	

	def get_queryset(self):
		queryset = Patient.objects.all()
		Patient_name = self.request.query_params.get('Patient_name',None)
		doctor_num =self.request.query_params.get('Patient_name',None)
		if Patient_name is not None:
			queryset = queryset.filter(Patient_name=Patient_name)
		return queryset

		





