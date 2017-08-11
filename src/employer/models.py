from django.db import models


class Employer(models.Model):
    JOB_TYPES = (
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        ('Internship', 'Internship'),
        ('Contract', 'Contract'),
        ('Other', 'Other'),
    )
    name = models.CharField(max_length=500, blank=False, null=False,
                            unique=True)
    city = models.CharField(max_length=100, blank=False, null=False)
    state = models.CharField(max_length=100, blank=False, null=False)
    web_url = models.CharField(max_length=500, blank=True, null=True)
    job_description = models.TextField()
    job_title = models.CharField(max_length=500, blank=False, null=False)
    job_type = models.CharField(max_length=100, choices=JOB_TYPES,
                                default='Other')

    class Meta:
        db_table = 'employer'
