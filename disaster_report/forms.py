from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *

mode_of_transport = [
  ("Driving","driving"),
  ("Bicycling","bicycling"),
  ("Walking","walking"),
  ("Transit","transit"),
]
class DisasterForm(ModelForm):

    class Meta:
        model = Disaster_report
        fields = ['name', 'zipcode', 'city', 'country', 'adress', 'latitude', 'longitude',  'images']