from django.contrib.auth import get_user_model
from .models import *
from django import forms
from django.forms import ModelForm

class VolunteerForm(ModelForm):

    class Meta:
        model = Volunteer
        fields = '__all__'

class ServiceForm(ModelForm):

    class Meta:
        model = Service
        fields = '__all__'

