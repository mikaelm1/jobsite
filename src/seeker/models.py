import logging
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

logger = logging.getLogger(__name__)


class Seeker(models.Model):
    user = models.OneToOneField(User)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


def create_seeker(sender, instance, created, **kwargs):
    if created:
        seeker = Seeker.objects.get_or_create(user=instance)
        logger.warning("Seeker: ({})".format(seeker))


post_save.connect(create_seeker, sender=User)