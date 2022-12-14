from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

# Options for different types of site, to determine which modules are available.
SITE_OPTIONS = (
    ('individual', "Individual Player"),
    ('club', "Single Club"),
    ('competition', "Single Competition"),
    ('multi', "Multiple Competitions"),
)


# Create your models here.

# Additional fields are added to the AbstractUser model.
class User(AbstractUser):
    objects = UserManager()
    organisation = models.CharField(max_length=50, blank=True, null=True)
    site_name = models.CharField(max_length=50, blank=True, null=True)
    site_type = models.CharField(max_length=25, choices=SITE_OPTIONS, blank=True, null=True)
    primary_color = models.CharField(max_length=10, blank=True, null=True, default="#ffffff")
    secondary_color = models.CharField(max_length=10, blank=True, null=True, default="#ffffff")
    primary_text = models.CharField(max_length=10, blank=True, null=True, default="#000000")
    secondary_text = models.CharField(max_length=10, blank=True, null=True, default="#000000")
    profile_picture = models.ImageField(upload_to="images/users", blank=True, null=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.username


class Sport(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=25)
    icon = models.ImageField(upload_to="images/sports", blank=True, null=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Continent(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=5)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=25)
    continent = models.ForeignKey(Continent, related_name='country_continent', on_delete=models.CASCADE, blank=True, null=True)
    abbreviation = models.CharField(max_length=5)
    is_active = models.BooleanField(default=True)
    is_independent = models.BooleanField(default=True)
    flag = models.ImageField(upload_to="images/countries")
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class State(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, related_name='state_country', on_delete=models.CASCADE)
    abbreviation = models.CharField(max_length=5)
    flag = models.ImageField(upload_to="images/states", blank=True, null=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class City(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=5)
    state = models.ForeignKey(State, related_name='city_state', on_delete=models.CASCADE)
    country = models.ForeignKey(Country, related_name='city_country', on_delete=models.CASCADE)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Venue(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100)
    city = models.ForeignKey(State, related_name='venue_city', on_delete=models.CASCADE)
    state = models.ForeignKey(State, related_name='venue_state', on_delete=models.CASCADE)
    country = models.ForeignKey(Country, related_name='venue_country', on_delete=models.CASCADE)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
