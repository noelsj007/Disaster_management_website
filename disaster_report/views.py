
import googlemaps
import gmaps
from datetime import datetime
from django.shortcuts import render, redirect, reverse
from .forms import *
from .models import *
from django.http import JsonResponse
from django.conf import settings
import requests
import json
import urllib
from .models import Disaster_report

# Create your views here.

def home(request):
    context = {}
    return render(request, 'home.html',context)


def geocode(request):
    clubs = Disaster_report.objects.all()
    context = {
        'clubs':clubs,
    }
    return render(request, 'geocode.html',context)

def geocode_club(request,pk):
    club = Disaster_report.objects.get(id=pk)
    # check whether we have the data in the database that we need to calculate the geocode
    if club.adress and club.country and club.zipcode and club.city != None: 
        # creating string of existing location data in database
        adress_string = str(club.adress)+", "+str(club.zipcode)+", "+str(club.city) +", "+str(club.country)
        print(adress_string)

        # geocode the string
        gmaps = googlemaps.Client(key= settings.GOOGLE_API_KEY)
        intermediate = json.dumps(gmaps.geocode(str(adress_string))) 
        intermediate2 = json.loads(intermediate)
        latitude = intermediate2[0]['geometry']['location']['lat']
        longitude = intermediate2[0]['geometry']['location']['lng']
        print(latitude)
        print(longitude)
        # save the lat and long in our database
        club.latitude = latitude
        club.longitude = longitude
        club.save()
        return redirect('geocode')
    else:
        return redirect('geocode')
    return render(request, 'empty.html',context)


def distance(request):
    gmaps = googlemaps.Client(key= settings.GOOGLE_API_KEY)
    now = datetime.now()
    calculate = json.dumps(gmaps.distance_matrix("Rat Verlegh Stadion",
                            "Breda Station",
                            mode="driving",
                            departure_time=now)) 
    calculate2 = json.loads(calculate)
    
    result = calculate2
    distance = calculate2['rows'][0]['elements'][0]['distance']['value']
    duration = calculate2['rows'][0]['elements'][0]['duration']['text']

    context = {
        'result':result,
        'distance':distance,
        'duration':duration
    }
    return render(request, 'distance.html',context)

def calculate_distance(request,pk,pk2):
    location1 = Disaster_report.objects.get(id=pk)
    location2 = Disaster_report.objects.get(id=pk2)

    result = Disaster_report.objects.all()
    context = {
        'result':result,
    }
    return render(request, 'distance.html',context)


def map(request):
    key = settings.GOOGLE_API_KEY
    form = DisasterForm
    context = {
        'key':key,
    }
    return render(request, 'map.html',context)


def mydata(request):
    result_list = list(Disaster_report().objects\
                .exclude(latitude__isnull=True)\
                .exclude(longitude__isnull=True)\
                .exclude(latitude__exact='')\
                .exclude(longitude__exact='')\
                .values('id',
                        'name', 
                        'latitude',
                        'longitude',
                        'attendance',
                        'stadium',
                        'country',
                        ))
  
    return JsonResponse(result_list, safe=False)