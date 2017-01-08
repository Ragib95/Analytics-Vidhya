from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Candidates(models.Model):
    serial_no = models.CharField(max_length=100)
    resume = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    work_experience = models.CharField(max_length=100)
    analytics_experience = models.CharField(max_length=100)
    current_loc = models.CharField(max_length=100)
    corrected_loc = models.CharField(max_length=100)
    nearest_city = models.CharField(max_length=100)
    preferred_loc = models.CharField(max_length=100)
    ctc = models.CharField(max_length=100)
    current_employer = models.CharField(max_length=200)
    current_designation = models.CharField(max_length=300)
    skills = models.CharField(max_length=1000)
    ug_course = models.CharField(max_length=100)
    ug_institute = models.CharField(max_length=500)
    ug_tier1 = models.CharField(max_length=100)
    ug_passing = models.CharField(max_length=100)
    pg_course = models.CharField(max_length=200)
    pg_institute = models.CharField(max_length=500)
    pg_tier1 = models.CharField(max_length=100)
    pg_passing = models.CharField(max_length=100)
    post_pg = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

