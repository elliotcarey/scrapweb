from django.db import models

# Create your models here.
class Immo(models.Model):
    price = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    typeImo = models.CharField(max_length=100)
    size = models.CharField(max_length=10)
    charac = models.CharField(max_length=100)