from datetime import date

from django.db import models


# Create your models here.
class MyPipelines(models.Model):
    prospectName = models.CharField(max_length=255)
    intermediaryName = models.CharField(max_length=255)
    premiumAmount = models.FloatField()
    businessClass = models.CharField(max_length=50)
    transactionDate = models.DateTimeField(default=date.today())
    closureDate = models.DateField()
    currentInsurer = models.CharField(max_length=255)
    likelyHood = models.CharField(max_length=5)
    status = models.CharField(max_length=20)
    remarks = models.TextField()
