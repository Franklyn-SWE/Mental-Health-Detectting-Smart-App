from django.shortcuts import render                                                   # FRANKLYN OLIHA  ID: 1611857

#Import HttpResponseRedirect - Http404 - HttpResponse
from django.http import HttpResponseRedirect, Http404, HttpResponse
#Restict files from non authenticated user using login_required decorator! 
from django.contrib.auth.decorators import login_required
#Import Permission Denied
from django.core.exceptions import PermissionDenied
#Import authenicate, login and logout from django contrib.auth
from django.contrib.auth import authenticate
#Import render - redirect
from django.shortcuts import render, redirect
#Import User for registration form!
from django.contrib.auth.models import User
#Import models from Main App
from Main.models import * 
#Import forms
from .forms import *
from django.urls import reverse

# STAFF REGISTRATION FORM
@login_required 
def staff_registration(request):

    if request.method == 'POST':
        user_form = StaffRegistrationForm(request.POST or None, files = request.FILES)
        if user_form.is_valid():
            new_user = User.objects.create(
                                username = user_form.cleaned_data['username'],
                                first_name = user_form.cleaned_data['first_name'],
                                last_name = user_form.cleaned_data['last_name'],
                                email = user_form.cleaned_data['email']                                
                            )         
            #random password creation
            password = User.objects.make_random_password()
            #set the password            
            new_user.set_password(password) 
         
            profile.objects.create(
                            user = new_user,
                            phone_number = user_form.cleaned_data['phone_number'],
                            staff_number = user_form.cleaned_data['staff_number'], 
                            date_of_birth = user_form.cleaned_data['date_of_birth'],                                                        
                            role = user_form.cleaned_data['role'],                                                         
                            )                                                   
                          
            new_user.save()        
            return redirect('../../../')
            
    else:
        user_form = StaffRegistrationForm()
    
    context = {       
        'user_form': user_form, 
        
    }
    return render(request,'staff/registration_form.html', context) 



from .forms import DiagnosisForm



# DIAGNOSIS ALGORITHM FORM
@login_required
def patient_diagnosis(request):
    if request.method == 'POST':
        form = DiagnosisForm(request.POST)
        if form.is_valid():
            # Get selected symptoms from form data
            selected_symptoms = form.cleaned_data['symptoms']
            
            # Get the corresponding mental illness based on the selected symptoms
            Mental_illness = mental_illness.objects.filter(symptoms__in=selected_symptoms).distinct().first()
            
            # Save the form data
            diagnosis = form.save(commit=False)
            diagnosis.staff_user = request.user
            
            # Save the mental illness to the diagnosis
            if Mental_illness is not None:
                diagnosis.mental_illness = Mental_illness
            else:
                # Handle case where no mental illness matches the selected symptoms
                return render(request, 'diagnosis_error.html')
            
            diagnosis.save()
    
            context = {
                'diagnosis': diagnosis,
            }
            
            # Redirect to the mental illness page
            return render(request, 'main/result.html', context)
    else:
        form = DiagnosisForm()
    
    context = {
        'form': form,
    }
    
    return render(request, 'staff/nurse_patient_form.html', context)


