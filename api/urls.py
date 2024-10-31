from django.contrib import admin
from django.urls import path, include

urlpatterns=[ path("auth/",include("usersapp.urls")),
	 path("",include("employee.urls")),

]