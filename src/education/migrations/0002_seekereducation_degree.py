# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-08 23:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seekereducation',
            name='degree',
            field=models.CharField(default='Other', max_length=100),
        ),
    ]
