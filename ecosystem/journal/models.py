from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
from django.conf import settings
from django.utils.text import slugify

import datetime



class School_subject(models.Model):

    name = models.CharField(max_length = 150)
    
    def __str__(self):
        return self.name




