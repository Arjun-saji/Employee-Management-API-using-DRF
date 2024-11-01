from .serializers import *
from .models import *
from rest_framework import generics,status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response



class EmployeeCreateView(generics.ListCreateAPIView):
	queryset=Employee.objects.all()
	serializer_class=EmployeeSerializer
	permission_class=[IsAuthenticated]



	def get_queryset(self):
		queryset=super().get_queryset()
		department=self.request.query_params.get('department')
		role=self.request.query_params.get('role')

		if department:
			queryset=queryset.filter(department=department)

		if role:
			queryset=queryset.filter(role=role)

		return queryset


	def create(self,request,*args,**kwargs):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			self.perform_create(serializer)
			return Response(serializer.data,status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
	queryset=Employee.objects.all()
	serializer_class=EmployeeSerializer
	permission_class=[IsAuthenticated]


	def delete(self,request,*args,**kwargs):
		response=super().delete(request,*args,**kwargs)
		if status==204:
			return Response({"message":"Employee Delete Sucessfully"},status=status.HTTP_204_NO_CONTENT)
		return response




