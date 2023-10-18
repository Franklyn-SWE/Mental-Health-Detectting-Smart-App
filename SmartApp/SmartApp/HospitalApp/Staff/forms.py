# FRANKLYN OLIHA  ID: 1611857

#Import User for registration form!
from django.contrib.auth.models import User
#Import Models from Main App
from Main.models import *
#Import forms
from django import forms
#Import date-time
from datetime import datetime
#Import timezone
from django.utils import timezone

#Staff Registration Form (Admin, Nurse, and Doctor)
class StaffRegistrationForm(forms.Form):
    ROLE_CHOICES = (
        ('Admin','Admin'),
        ('Nurse','Nurse'),
        ('Doctor','Doctor'),
    )
    username = forms.CharField(widget=forms.TextInput(attrs={'required': True})) 
    first_name = forms.CharField(widget=forms.TextInput(attrs={'required': True})) 
    last_name = forms.CharField(widget=forms.TextInput(attrs={'required': True})) 		
    email = forms.EmailField(widget=forms.TextInput(attrs={'required': True}))
    staff_number = forms.CharField(widget=forms.TextInput(attrs={'required': True}))
    date_of_birth = forms.DateField(widget = forms.DateInput(attrs={'type': 'date'}))    
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'required': True})) 
    role = forms.ChoiceField(choices = ROLE_CHOICES)    
    #house_number = forms.CharField(widget=forms.TextInput(attrs={'required': True}))
    #street_name = forms.CharField(widget=forms.TextInput(attrs={'required': True}))
    #city = forms.CharField(widget=forms.TextInput(attrs={'required': True}))
    #postcode = forms.CharField(widget=forms.TextInput(attrs={'required': True}))               
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email = email).exists():
            raise forms.ValidationError('Email already exists!' % email)    
        return email  
        
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username = username).exists():
            raise forms.ValidationError('Username " %s " is already in use!' % username)
        return username

# DIAGNOSIS FORM
class DiagnosisForm(forms.ModelForm):
    symptoms = forms.ModelMultipleChoiceField(
        queryset=symptom.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    # PATIENTS INFORMATION ATTARCHED TO DIAGNOSIS 
    class Meta:
        model = diagnosis
        fields = ['firstname', 'lastname', 'patient_number', 'symptoms']
        labels = {
            'firstname': "Patient's Name",
            'lastname': "Patient's Surname",
            'patient_number': "Patient's Number",
        }
