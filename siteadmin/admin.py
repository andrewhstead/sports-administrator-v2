from django.contrib import admin
from .models import User, Sport, Country, State, City, Venue

# Register your models here.
admin.site.register(User)
admin.site.register(Sport)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Venue)
