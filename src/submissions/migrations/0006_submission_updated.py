# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 20:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0005_submission_total_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
