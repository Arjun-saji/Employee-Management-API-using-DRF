from django.urls import path
from . import views

urlpatterns=[path('employees/', views.EmployeeCreateView.as_view(), name='employee-list-create'),
	path('employees/<int:pk>/', views.EmployeeRetrieveUpdateDeleteView.as_view(), name='employee-retrieve-update-delete'),]