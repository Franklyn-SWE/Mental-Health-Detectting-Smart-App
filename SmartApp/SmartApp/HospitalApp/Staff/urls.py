
#Staff App URLS

from django.urls import path
from . import views

app_name= 'staff_app'

urlpatterns = [
    path('staff/registration/', views.staff_registration, name = 'staff_registration'), 
    #path('diagnose/', views.diagnosis_form, name="diagnose"),
    path('patient_diagnosis/', views.patient_diagnosis, name='patient_diagnosis'),
   
    
]

