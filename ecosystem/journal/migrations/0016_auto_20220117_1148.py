# Generated by Django 3.2.11 on 2022-01-17 11:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0015_auto_20220117_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school_subject',
            name='end_time',
            field=models.TimeField(default=datetime.time(11, 48, 21, 132819)),
        ),
        migrations.AlterField(
            model_name='school_subject',
            name='start_time',
            field=models.TimeField(default=datetime.time(11, 48, 21, 132801)),
        ),
    ]
