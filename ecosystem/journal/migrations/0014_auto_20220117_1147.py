# Generated by Django 3.2.11 on 2022-01-17 11:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0013_auto_20220117_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school_subject',
            name='end_time',
            field=models.TimeField(default=datetime.time(11, 47, 30, 850574)),
        ),
        migrations.AlterField(
            model_name='school_subject',
            name='start_time',
            field=models.TimeField(default=datetime.time(11, 47, 30, 850556)),
        ),
    ]
