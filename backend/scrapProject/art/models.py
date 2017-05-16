from django.db import models

# Create your models here.
class Art(models.Model):
    date = models.CharField(max_length=100)
    typeart = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)