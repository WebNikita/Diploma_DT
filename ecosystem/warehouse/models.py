from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
from accounts.models import Teacher
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=256, db_index=True)
    slug = models.SlugField(max_length=256, unique=True)
    # class Meta:
    #     ordering = ('name',)
    #     verbose_name = 'category'
    #     verbose_name_plural = 'categories'
    
    # def __str__(self):
    #     return self.name
class Extradition(models.Model):
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
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
    # user = models.CharField(max_length=128)

class Warehouse(models.Model):
    category = models.ForeignKey(Category,
                                related_name='product',
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=128, db_index=True)
    slug = models.SlugField(max_length=128, db_index=True)
    cell = models.CharField(max_length=128)
    remains = models.IntegerField()
    # remains = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # class Meta:
    #     ordering = ('name',)
    #     index_together = (('id', 'slug'),)
    # def __str__(self):
    #     return self.name