# Generated by Django 3.2.11 on 2022-01-08 15:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0007_auto_20220107_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school_subject',
            name='end_time',
            field=models.TimeField(default=datetime.time(15, 32, 37, 157383)),
        ),
        migrations.AlterField(
            model_name='school_subject',
            name='start_time',
            field=models.TimeField(default=datetime.time(15, 32, 37, 157366)),
        ),
    ]
