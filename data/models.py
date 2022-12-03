from django.db import models
from siteadmin.models import Sport, Country


# Create your models here.
class Competition(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100)
    sport = models.ForeignKey(Sport, related_name='competition_sport', on_delete=models.CASCADE)
    country = models.ForeignKey(Country, related_name='competition_country', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
