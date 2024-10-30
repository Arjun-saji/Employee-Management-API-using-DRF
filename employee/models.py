# from django.db import models

# # Create your models here.

# class Employee(models.Model):
# 	name=models.Charfield(max_length=200)
# 	email =models.EmailField()
# 	department=models.Charfield(max_length=50,choices=(
# 		('HR','hr'),
# 		('ENGINEER',"engineer"),
# 		('SALES','sales')
# 		),blank=True,null=True)
# 	role=models.Charfield(max_length=30,choices=(
# 		('MANAGER','manager'),
# 		('DEVELOPER',"developer"),
# 		('ANALYST','analyst')
# 		),blank=True,null=True)
# 	date_joined=models.DateTimeField(auto_now_add=True)


# 	def __str__(self):
# 		return f"{self.name}"
