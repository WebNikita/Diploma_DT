from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.text import slugify
import datetime

class  Student(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, null=False)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length = 13)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)

class  Teacher(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, null=False)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length = 13)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)