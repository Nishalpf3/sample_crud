# employee_project/urls.py

from django.contrib import admin
from django.urls import path, include
from employee_register import views  # Import the home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/', include('employee_register.urls')),  # Include the employee app's URLs
    path('', views.home, name='home'),  # Define root URL to use the home view
]
