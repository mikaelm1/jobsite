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

    def __str__(self):
        return self.name


class SeekerEducation(models.Model):
    year_started = models.IntegerField()
    year_ended = models.IntegerField()
    graduated = models.BooleanField()
    major = models.CharField(max_length=250, default='Other')
    seeker = models.ForeignKey(Seeker, on_delete=models.CASCADE)
    education = models.ForeignKey(Education, on_delete=models.CASCADE)

    class Meta:
        db_table = 'seeker_education'

    def __str__(self):
        return str(self.year_ended)
