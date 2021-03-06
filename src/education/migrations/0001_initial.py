# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-08 04:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('seeker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=250, unique=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'education',
            },
        ),
        migrations.CreateModel(
            name='SeekerEducation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_started', models.IntegerField()),
                ('year_ended', models.IntegerField()),
                ('graduated', models.BooleanField()),
                ('major', models.CharField(default='Other', max_length=250)),
                ('education', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.Education')),
                ('seeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seeker.Seeker')),
            ],
            options={
                'db_table': 'seeker_education',
            },
        ),
    ]
