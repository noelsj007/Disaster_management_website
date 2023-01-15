from . import views
from django.urls import path, include
# from disaster_report import views as view

urlpatterns = [
   path('',views.home, name="home"),
   path('geocode',views.geocode, name="geocode"),
   path('geocode/club/<int:pk>',views.geocode_club, name="geocode_club"),

   path('distance',views.distance, name="distance"),
   path('map',views.map, name="map"),
   path('mydata',views.mydata, name="mydata"),
   path('calculate/distance/<int:pk>/<int:pk2>',views.calculate_distance, name="calculate_distance"),
]