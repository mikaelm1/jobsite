from django.db import models
from seeker.models import Seeker


class Experience(models.Model):
    JANUARY = 'Jan'
    FEBRUARY = 'Feb'
    MARCH = 'Mar'
    APRIL = 'Apr'
    MAY = 'May'
    JUNE = 'Jun'
    JULY = 'Jul'
    AUGUST = 'Aug'
    SEPTEMBER = 'Sep'
    OCTOBER = 'Oct'
    NOVEMBER = 'Nov'
    DECEMBER = 'Dec'
    MONTHS = (
        (JANUARY, JANUARY),
        (FEBRUARY, FEBRUARY),
        (MARCH, MARCH),
        (APRIL, APRIL),
        (MAY, MAY),
        (JUNE, JUNE),
        (JULY, JULY),
        (AUGUST, AUGUST),
        (SEPTEMBER, SEPTEMBER),
        (OCTOBER, OCTOBER),
        (NOVEMBER, NOVEMBER),
        (DECEMBER, DECEMBER),
    )
    title = models.CharField(max_length=500, blank=False, null=False)
    company_name = models.CharField(max_length=500, blank=False, null=False)
    job_description = models.TextField()
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    start_month = models.CharField(max_length=50, blank=False, null=False,
                                   choices=MONTHS, default=JANUARY)
    end_month = models.CharField(max_length=50, blank=True, null=True,
                                 choices=MONTHS, default=JANUARY)
    present = models.BooleanField(default=False)
    seeker = models.ForeignKey(Seeker, on_delete=models.CASCADE)

    class Meta:
        db_table = 'experience'

    def __str__(self):
        return str(self.title)
