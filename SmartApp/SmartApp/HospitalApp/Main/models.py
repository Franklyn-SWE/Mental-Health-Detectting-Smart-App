from django.db import models                                                                                  # FRANKLYN OLIHA  ID: 1611857
#Import user from django contrib in order to use
from django.contrib.auth.models import User
#Import timezones for date time
from django.utils import timezone

#PROFILE
class profile(models.Model):
    ROLE_CHOICES = (
        ('Admin','Admin'),
        ('Nurse','Nurse'),
        ('Doctor','Doctor'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True, related_name = 'profile')
    date_of_birth = models.DateField()	
    staff_number = models.CharField(max_length = 20)
    phone_number = models.CharField(max_length = 15) 
    role = models.CharField(max_length = 15, choices = ROLE_CHOICES, default = 'Admin')
    
    def __str__(self):
        return "profile of user {} {}".format(self.user.first_name, self.user.last_name)

# SYMPTOMS 
class symptom(models.Model):
    symptom_name = models.CharField('Symptom', max_length = 100) 
    def __str__(self):
        return "Symptom: %s" % (self.symptom_name)
        
# MENTAL ILLNESS 
class mental_illness(models.Model):
    mental_illness_name  = models.CharField('Mental Illness Name', max_length = 150) 
    description = models.CharField('Description', max_length = 1000) 
    symptoms = models.ManyToManyField(symptom, related_name = 'mental_illnesses') 
    def __str__(self):
        return "Mental Illness: %s" % (self.mental_illness_name)
    class Meta:
        verbose_name_plural = "Mental Illness" 
        
#  DIAGNOSIS 
class diagnosis(models.Model):
    firstname = models.CharField("Patient's Name", max_length = 30)
    lastname = models.CharField("Patient's Surname", max_length = 30) 
    patient_number = models.CharField("Patient's Number", max_length = 20)  
    mental_illness = models.ForeignKey(mental_illness, on_delete=models.SET_NULL, null=True, related_name = 'mental_illness') 
    symptoms = models.ManyToManyField(symptom, related_name = 'diagnoses') 
    staff_user = models.ForeignKey(User, on_delete = models.CASCADE)
    approved = models.BooleanField(default = False)
    timestamp = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return "Patient's Name: %s %s - Diagnosis: %s" % (self.firstname, self.lastname, self.mental_illness.mental_illness_name)    
    class Meta:
        verbose_name_plural = "Diagnosis"     
        

class message(models.Model):
    send = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'send')
    receive = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'receive')
    receive_email = models.EmailField()
    title = models.CharField(max_length = 30)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
        
        
        
        

 