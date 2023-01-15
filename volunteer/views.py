from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import *
from .models import *
from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance

longitude = 11.881864
latitude = 75.394191

user_location = Point(longitude, latitude, srid=4326)


class NearVolunteer(generic.ListView):
    model = CustomUser
    context_object_name = 'shops'
    queryset = CustomUser.objects.annotate(distance=Distance('location',
    user_location)
    ).order_by('distance')[0:3]
    template_name = 'nearvolunteers.html'

longitude = 12.881864
latitude = 76.394191
service_location = Point(longitude, latitude, srid=4326)

class NearService(generic.ListView):
    model = ServiceAdmin
    context_object_name = 'service'
    queryset = ServiceAdmin.objects.annotate(distance=Distance('serviceadmin_locations',
    service_location)
    ).order_by('distance')[0:3]
    template_name = 'nearservice.html'

# Create your views here.


# @login_required(login_url='login')
def homePage(request):
    return render(request, 'index.html')


def VolunteerRegisterPage(request):

    form = VolunteerForm()
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()


            # messages.success(request, 'Account Created for ' + user + ' Please login')
            return redirect('home')
    return render(request, 'volunteerregister.html', {'form': form})

def ServiceRegisterPage(request):

    form = ServiceForm()
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()


            # messages.success(request, 'Account Created for ' + user + ' Please login')
            return redirect('home')
    return render(request, 'serviceregister.html', {'form': form})


