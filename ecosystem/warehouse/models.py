from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Extradition(models.Model):
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    cell = models.CharField(max_length=128)
    quantity = models.IntegerField()
    data = models.DateTimeField()
    user = models.CharField(max_length=128)

class Shipment(models.Model):
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    cell = models.CharField(max_length=128)
    quantity = models.IntegerField()
    data = models.DateField()
    # user = models.CharField(max_length=128)
class Warehouse(models.Model):
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    cell = models.CharField(max_length=128)
    quantity = models.IntegerField()
    remains = models.IntegerField()
    data = models.DateTimeField()