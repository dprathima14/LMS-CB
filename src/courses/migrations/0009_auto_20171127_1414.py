# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 19:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_auto_20171127_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='syllabus',
            field=models.FileField(blank=True, max_length=200, null=True, upload_to=''),
        ),
    ]
