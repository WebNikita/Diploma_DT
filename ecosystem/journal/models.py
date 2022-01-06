from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.text import slugify
from accounts.models import Student, Teacher

import datetime



class School_subject(models.Model):

    DAY_CHOICES = (
        ('M','Понедельник'),
        ('Tu','Вторник'),
        ('W','Среда'),
        ('Th','Четверг'),
        ('F','Пятница')
    )

    WEEK_TYPE_CHOICES = (
        ('NUM','Числитель'),
        ('DEN','Знаменатель'),
    )

    name = models.CharField(max_length = 150)
    day = models.CharField(max_length = 15 ,choices = DAY_CHOICES, default = 'M')
    start_time = models.TimeField(default=datetime.datetime.now().time())
    end_time = models.TimeField(default=datetime.datetime.now().time())
    week_type = models.CharField(max_length = 15 ,choices = WEEK_TYPE_CHOICES, default = 'NUM')

class Group(models.Model):
    shcool = models.CharField(max_length = 150)
    auditorium = models.IntegerField(max_length = 15)
    teachers = models.ManyToManyField(
        Teacher,
        related_name='group'
    )
    
    student = models.ManyToManyField(
        Student,
        related_name='group'
    )

    school_subject = models.ManyToManyField(
        School_subject,
        related_name='group'
    )
