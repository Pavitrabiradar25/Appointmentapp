from appointmentapp.models import *
from rest_framework import serializers


class DoctorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Doctor
		fields='__all__'

class PatientSerializer(serializers.ModelSerializer):
	class Meta:
		model = Patient
		fields='__all__'

class AppointmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Appointment
		fields='__all__'
