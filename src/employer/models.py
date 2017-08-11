from django.db import models
from django.contrib.auth.models import User


class Employer(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=500, blank=False, null=False,
                            unique=True)
    city = models.CharField(max_length=100, blank=False, null=False)
    state = models.CharField(max_length=100, blank=False, null=False)
    web_url = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = 'employer'

    def __str__(self):
        return str(self.name)
