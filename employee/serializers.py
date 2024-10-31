from rest_framework import serializers
from . models import *



class EmployeeSerializer(serializers.ModelSerializer):
	name = serializers.CharField(required=True, error_messages={"required": "Name cannot be empty."})
	email = serializers.EmailField(required=True, error_messages={"required": "Email cannot be empty."})
	class Meta:
		model=Employee
		fields = '__all__'
		

	def validate_email(self,value):
		if Employee.objects.filter(email=value).exists():
			raise serializers.ValidationError("Email already in use.")
		return value


