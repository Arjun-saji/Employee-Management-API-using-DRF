from django.db import models


class Employee(models.Model):
	name=models.CharField(max_length=200,blank=False)
	email =models.EmailField(unique=True) 
	department=models.CharField(max_length=50,choices=(
			('HR', 'HR'),
			('ENGINEER', 'Engineer'),
			('SALES', 'Sales')
		),blank=True,null=True)
	role = models.CharField(max_length=30, choices=(
		('MANAGER', 'manager'),
		('DEVELOPER', 'developer'),
		('ANALYST', 'analyst'), 
	), blank=True, null=True)
	date_joined=models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return f"{self.name}"
