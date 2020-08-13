from django.db import models

# Create your models here.


class ActivityPeriods(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


class Members(models.Model):
    id = models.CharField(max_length=9, primary_key=True, editable=False)
    real_name = models.CharField(max_length=50)
    tz = models.CharField(max_length=35)
    activity_periods = models.ManyToManyField(ActivityPeriods)