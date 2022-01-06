from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.text import slugify
import datetime


# class  Profile(models.Model):

#     TYPE_CHOICES = (
#         ('Student',' Студент'),
#         ('Teacher','Преподаватель'),
#     )

#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     slug = models.SlugField(unique=True, null=False)
#     date_of_birth = models.DateField()
#     phone_number = models.CharField(max_length = 13)
#     type_of_user = models.CharField(max_length = 15 ,choices = TYPE_CHOICES, default = 'Student')

#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.user.username)
#         super().save(*args, **kwargs)

# class School_subject(models.Model):

#     DAY_CHOICES = (
#         ('M','Понедельник'),
#         ('Tu','Вторник'),
#         ('W','Среда'),
#         ('Th','Четверг'),
#         ('F','Пятница')
#     )

#     WEEK_TYPE_CHOICES = (
#         ('NUM','Числитель'),
#         ('DEN','Знаменатель'),
#     )

#     name = models.CharField(max_length = 150)
#     day = models.CharField(max_length = 15 ,choices = DAY_CHOICES, default = 'M')
#     time = models.TimeField(default=datetime.datetime.now().time())
#     week_type = models.CharField(max_length = 15 ,choices = WEEK_TYPE_CHOICES, default = 'NUM')
#     classroom = models.CharField(max_length = 150, null=True)
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
