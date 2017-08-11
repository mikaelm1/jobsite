from django.db import models
from django.utils.timezone import now
from employer.models import Employer


class Job(models.Model):
    JOB_TYPES = (
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        ('Internship', 'Internship'),
        ('Contract', 'Contract'),
        ('Other', 'Other'),
    )
    title = models.CharField(max_length=500, blank=False, null=False)
    job_description = models.TextField()
    job_type = models.CharField(max_length=100, choices=JOB_TYPES,
                                default='Other')
    salary_min = models.IntegerField(blank=True, null=True)
    salary_max = models.IntegerField(blank=True, null=True)
    date_posted = models.DateTimeField(default=now)
    visible = models.BooleanField(default=True)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)
