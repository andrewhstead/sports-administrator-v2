from django.db import models


# Create your models here.
class Sport(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=25)
    icon = models.ImageField(upload_to="images/sports", blank=True, null=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=25)
    abbreviation = models.CharField(max_length=5)

    def __str__(self):
        return self.name


class State(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, related_name='state_country', on_delete=models.CASCADE)
    abbreviation = models.CharField(max_length=5)

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
