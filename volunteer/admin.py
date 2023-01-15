from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import CustomUser, Volunteer, Service, ServiceAdmin
# Register your models here.

@admin.register(CustomUser)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('email', 'location')
@admin.register(ServiceAdmin)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('serviceadmin_name', 'serviceadmin_locations')

admin.site.register(Volunteer)
admin.site.register(Service)

