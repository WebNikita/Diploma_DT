# Generated by Django 4.0.1 on 2022-01-05 19:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0002_school_subject_time_school_subject_week_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='school_subject',
            name='classroom',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='school_subject',
            name='time',
            field=models.TimeField(default=datetime.time(19, 14, 24, 661100)),
        ),
    ]
