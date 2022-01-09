from django.db import models
from django.utils import timezone
from django.conf import settings
from django.db.models.fields.related import ForeignKey
from django.utils.text import slugify
import datetime

from journal.models import School_subject


class  Teacher(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, null=False)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length = 13)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

class Group(models.Model):

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

    shcool = models.CharField(max_length = 150)
    auditorium = models.IntegerField(max_length = 15)
    day = models.CharField(max_length = 15 ,choices = DAY_CHOICES, default = 'M')
    start_time = models.TimeField(default=datetime.datetime.now().time())
    end_time = models.TimeField(default=datetime.datetime.now().time())
    week_type = models.CharField(max_length = 15 ,choices = WEEK_TYPE_CHOICES, default = 'NUM')
    school_subject = ForeignKey(School_subject, on_delete = models.CASCADE, null=True)
    teacher = ForeignKey(Teacher, on_delete = models.CASCADE, null=True)

    def __str__(self):
        return self.shcool


class  Student(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, null=False)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length = 13)
    group = models.ManyToManyField(Group, null = True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)
    


    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'