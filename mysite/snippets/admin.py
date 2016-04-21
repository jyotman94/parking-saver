from django.contrib import admin
from .models import Location

class LocationAdmin(admin.ModelAdmin):
	list_display = ('owner', 'address', 'created', 'retrieved')

admin.site.register(Location, LocationAdmin)
