from django.db import models

# Create your models here.
class Gecko(models.Model):
    name = models.CharField(max_length=100)
    genus = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    locale_subspecies = models.CharField(max_length=100)
    discovered = models.CharField(null=True, max_length=300)
    description = models.CharField(max_length=500)
    habitat = models.CharField(max_length=200)
    snout_to_vent = models.CharField(max_length=200)
    lifespan = models.CharField(max_length=200)
    species_range = models.CharField(max_length=200)
    geoLocation = models.CharField(max_length=200)

    def __str__(self):
        return self.name
