from django.db import models
from django.contrib.auth.models import User


class Seeker(models.Model):
    user = models.OneToOneField(User)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
