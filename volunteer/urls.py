from django.views.generic import TemplateView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('volunteerregister/', views.VolunteerRegisterPage, name='volunteerregister'),
    path('serviceregister/', views.ServiceRegisterPage, name='serviceregister'),
    path('nearvolunteers/', views.NearVolunteer.as_view(), name='nearvolunteer'),
    path('nearservice/', views.NearService.as_view(), name='serviceadmin')
]