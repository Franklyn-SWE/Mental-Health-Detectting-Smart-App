#Import JsonResponse - JsonResponse - HttpResponseRedirect - HttpResponse                              # FRANKLYN OLIHA  ID: 1611857
from datetime import datetime
from django.http import Http404, JsonResponse, HttpResponseRedirect, HttpResponse
#Import django user authentication and login!
from django.contrib.auth import authenticate, login, logout
#Import Permission-Denied
from django.core.exceptions import PermissionDenied
#Import login required
from django.contrib.auth.decorators import login_required
#Import - Render - Redirect
from django.shortcuts import render, redirect
#Import User
from django.contrib.auth.models import User 
#Import Views
from .models import *
#Import forms
from .forms import * 



#Dashboard redirections!
@login_required
def index(request):
    
    try:  
        user_id = request.user.id
        
        logged_in_user = profile.objects.get(user__id = user_id)
    
    except profile.DoesNotExist:
        raise Http404("Requested profile does not exist!")
    
    if logged_in_user.role == 'Nurse':
        return redirect('../../../nurse_dashboard/') 
        
    elif logged_in_user.role == 'Doctor':
        return redirect('../../../doctor_dashboard/') 

    elif logged_in_user.role == 'Admin':
        return redirect('../../../admin_dashboard/')  

    else:
        raise PermissionDenied

       
#Nurse Dashboard 
@login_required       
def nurse_dashboard(request):

    context = {
    
        
    }
    return render(request, 'main/nurse_dashboard.html', context)   


#Doctor Dashboard 
@login_required
def doctor_dashboard(request):

    context = {
    
        
    }
    return render(request, 'main/doctor_dashboard.html', context)  


#Admin Dashboard  
@login_required 
def admin_dashboard(request):

    context = {
    
        
    }
    return render(request, 'main/admin_dashboard.html', context)  
    
 # Login User
def userLogin(request):
 
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            #Check if the user name is there and password!
            #'authenticate' checks the user's credentials    
            user = authenticate(username = username, password = password) 
            if user is not None:
                login(request, user) 
                #Redirect to the index.html page 
                return redirect('../../../') 
                
            else:
                return redirect('/accounts/login/')
                
    #If form is not valid or empty!
    else:
        form = UserLoginForm()
        
    context = {
    
        'form': form
        
    }
    return render(request, 'main/login.html', context) 

# List of Mental Illness and Symptoms 
@login_required
def illnesses_list(request):
    
    try:  
        
        all_illnesses = mental_illness.objects.all()
    
    except profile.DoesNotExist:
        raise Http404("Requested profile does not exist!")
    
    context = {
    
        'all_illnesses': all_illnesses
        
    }
    return render(request, 'main/list_mental_illnesses.html', context) 



       
#Logout User
@login_required 			
def logout_user(request):
    logout(request)
    return redirect('../../../accounts/login/')    





# Sending Messages 
@login_required
def send_message(request):
    if request.method == 'POST':
        form = CreateMessage(request.POST)
        if form.is_valid:
            message_item = form.save(commit=False)
            message_item.send = request.user
            receive_email = form.cleaned_data.get('receive_email')
            message_item.receive = User.objects.get(email = receive_email)
            message_item.date = datetime.now()
            message_item.save()
            return redirect('../../../')

            #return render(request, 'main/nurse_dashboard.html')
    else:
        form = CreateMessage() #(request.POST)
        return render(request, 'main/send_message.html', {'form' : form})
    
# Receive and View Messages 
@login_required
def view_messages(request):
    all_messages = message.objects.order_by('-date')
    list_of_messages = []
    for x in all_messages:
        if x.send != None and x.receive != None:
            if x.receive.email == request.user.email:
                list_of_messages.append(x)
    return render(request, 'main/view_messages.html', {'list_of_messages' : list_of_messages})

# View Patients Diagnosis Results 
@login_required
def result(request):
    all_patients = diagnosis.objects.all()

    return render(request, 'main/view_patients.html', {'all_patients' : all_patients})


