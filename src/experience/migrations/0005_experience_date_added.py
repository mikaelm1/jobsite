# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-10 04:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0004_experience_seeker'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
