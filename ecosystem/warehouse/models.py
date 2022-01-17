from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
from accounts.models import Teacher
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=256, db_index=True)
    slug = models.SlugField(max_length=256, unique=True)

class Warehouse(models.Model):
    category = models.ForeignKey(Category,
                                related_name='products',
                                on_delete=models.CASCADE,
                                null=True)
    name = models.CharField(max_length=256, db_index=True)
    slug = models.SlugField(max_length=256, db_index=True, null=True)
    cell = models.CharField(max_length=128)
    remains = models.IntegerField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

class Extradition(models.Model):
    # category = models.ForeignKey(Category,
    #                             related_name='products',
    #                             on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    cell = models.CharField(max_length=128)
    quantity = models.IntegerField()
    data = models.DateTimeField()
    user_id = models.ManyToManyField(
        Teacher,
        related_name='extradition'
    )

# class Shipment(models.Model):
#     name = models.CharField(max_length=128)
#     type = models.CharField(max_length=128)
#     cell = models.CharField(max_length=128)
#     quantity = models.IntegerField()
#     data = models.DateField()