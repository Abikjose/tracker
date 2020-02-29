from django.db import models

# Create your models here.
class Tracker_incident(models.Model):
    date          = models.CharField(max_length=120)
    issue         = models.CharField(max_length=120)
    description   = models.CharField(max_length=120)
    severity      = models.CharField(max_length=120)
    reporter      = models.CharField(max_length=120)
    owner         = models.CharField(max_length=120)
    status        = models.CharField(max_length=120)
    comments      = models.CharField(max_length=120)
    occ           = models.CharField(max_length=120)
    def __str__(self):
        return  self.date
