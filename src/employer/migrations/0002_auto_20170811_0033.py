# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-11 00:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employer',
            name='job_description',
        ),
        migrations.RemoveField(
            model_name='employer',
            name='job_title',
        ),
        migrations.RemoveField(
            model_name='employer',
            name='job_type',
        ),
    ]
