from django.contrib import admin
#Import everything from models
from .models import *


# Models registration.
admin.site.register(profile)
admin.site.register(symptom)
admin.site.register(diagnosis)
admin.site.register(mental_illness)
admin.site.register(message)

