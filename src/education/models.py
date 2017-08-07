from django.db import models
from seeker.models import Seeker


class EducationManager(models.Manager):
    pass


class Education(models.Model):
    name = models.CharField(max_length=250, unique=True, db_index=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    # objects = EducationManager()

    class Meta:
        db_table = 'education'


class SeekerEducation(models.Model):
    year_started = models.IntegerField()
    year_ended = models.IntegerField()
    graduated = models.BooleanField()
    seeker = models.ManyToManyField(Seeker)
    education = models.ForeignKey(Education)

    class Meta:
        db_table = 'seeker_education'
