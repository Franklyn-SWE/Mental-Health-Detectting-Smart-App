
#Main App URLS

from django.urls import path, include
from . import views

app_name= 'main_app'

urlpatterns = [
    path('', views.index, name = 'index'),
	path('accounts/login/', views.userLogin, name = "userLogin"), 
	path('logout/', views.logout_user, name = 'logout_user'),    
	path('nurse_dashboard/', views.nurse_dashboard, name = "nurse_dashboard"),    
	path('send_message/', views.send_message, name = "send_message"),       
	path('view_messages/', views.view_messages, name = "view_messages"),     
	path('doctor_dashboard/', views.doctor_dashboard, name = "doctor_dashboard"),  
	path('admin_dashboard/', views.admin_dashboard, name = "admin_dashboard"),       
	path('list_all_illnesses/', views.illnesses_list, name = "list_all_illnesses"), 
    path('index/', views.index, name = "index"),
	path('diagnosis/<int:pk>/', views.diagnosis, name='diagnosis'),  
    
    path('result/', views.result, name = "result"), 
	    
]

