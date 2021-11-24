from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length = 13)
    email = models.EmailField()


class School_subject(models.Model):

    DAY_CHOICES = (
        ('M','Понедельник'),
        ('Tu','Вторник'),
        ('W','Среда'),
        ('Th','Четверг'),
        ('F','Пятница')
    )

    name = models.CharField(max_length = 150)
    day = models.CharField(max_length = 15 ,choices = DAY_CHOICES, default = 'M')

# class Group(models.Model):
#     shcool = models.CharField(max_length = 150)
#     teachers = models.ManyToManyField(
#         Teacher,
#         related_name='group'
#     )
#     school_subject = models.ManyToManyField(
#         School_subject,
#         related_name='group'
#     )

# class Turnout(models.Model):
#     data = models.DateField()
#     student = models.ManyToManyField(
#         Student,
#         related_name='turnout'
#     )
#     school_subject = models.ManyToManyField(
#         School_subject,
#         related_name='turnout'
    # )
