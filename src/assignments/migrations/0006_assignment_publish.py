# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 23:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0005_auto_20171201_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='publish',
            field=models.BooleanField(default=False),
        ),
    ]