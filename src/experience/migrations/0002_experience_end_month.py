# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-09 04:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='end_month',
            field=models.CharField(blank=True, choices=[('Jan', 'Jan'), ('Feb', 'Feb'), ('Mar', 'Mar'), ('Apr', 'Apr'), ('May', 'May'), ('Jun', 'Jun'), ('Jul', 'Jul'), ('Aug', 'Aug'), ('Sep', 'Sep'), ('Oct', 'Oct'), ('Nov', 'Nov'), ('Dec', 'Dec')], default='Jan', max_length=50, null=True),
        ),
    ]