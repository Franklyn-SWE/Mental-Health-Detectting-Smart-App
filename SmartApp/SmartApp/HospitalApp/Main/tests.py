"""
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from .models import profile, mental_illness, symptom, diagnosis , message

"""

from django.test import TestCase

from django.contrib.auth.models import User

from django.urls import reverse

from .models import profile

from django.test import TestCase
from django.contrib.auth.models import User
from Main.models import Profile



class ProfileTestCase(TestCase):
    def setUp(self):
     self.user = User.objects.create_user(username='testuser', password='testpass')
     self.profile = Profile.objects.create(user=self.user, date_of_birth='2000-01-01')



    def test_profile_date_of_birth(self):
        
        self.assertEqual(str(self.profile.date_of_birth), '2000-01-01')


class TestIndexView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

        self.profile = profile.objects.create(user=self.user, role='Nurse')


    def test_nurse_redirect(self):
        
        self.client.login(username='testuser', password='12345')

        response = self.client.get(reverse('index'))
 
        self.assertRedirects(response, reverse('nurse_dashboard'), status_code=302, target_status_code=200)


def test_doctor_redirect(self):
    
    self.profile.role = 'Doctor'

    self.profile.save()

    self.client.login(username='testuser', password='12345')

    response = self.client.get(reverse('index'))

    self.assertRedirects(response, reverse('doctor_dashboard'), status_code=302, target_status_code=200)



def test_admin_redirect(self):
        
        self.profile.role = 'Admin'
        
        self.profile.save()

        self.client.login(username='testuser', password='12345')

        response = self.client.get(reverse('index'))

        self.assertRedirects(response, reverse('admin_dashboard'), status_code=302, target_status_code=200)



def test_permission_denied(self):
    
     self.profile.role = 'InvalidRole'

     self.profile.save()

     self.client.login(username='testuser', password='12345')

     response = self.client.get(reverse('index'))

     self.assertEqual(response.status_code, 403)










