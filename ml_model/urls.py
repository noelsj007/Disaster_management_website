# 

from django.views.generic import TemplateView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Validate_disaster, name='validate_disaster'),
]