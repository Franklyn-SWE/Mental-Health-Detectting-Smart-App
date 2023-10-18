# FRANKLYN OLIHA  ID: 1611857

#Import User for registration form!
from django.contrib.auth.models import User
#Import Models
from Main.models import *
#Import forms
from django import forms


#Create a class for login page!!
class UserLoginForm(forms.Form):
	username = forms.CharField(label="Username")
	#Use a widget otherwise password will be visible to everyone!
	password  = forms.CharField(label="Password", widget=forms.PasswordInput ) 

class CreateMessage(forms.ModelForm):
	title = forms.CharField(max_length=30)
	body = forms.CharField(widget=forms.Textarea)
	receive_email = forms.EmailField()
	class Meta:
		model = message
		fields = ('receive_email', 'title', 'body')