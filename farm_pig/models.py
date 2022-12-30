from django.db import models
from django.conf import settings
from users.models import Company

import datetime


class ReproductionStage(models.Model):
    stage = models.CharField(max_length=100)
    def __str__(self):
        return str(self.stage)

# Create your models here.
class Pig(models.Model):
    company = models.ForeignKey(
        Company, related_name="order_items", on_delete=models.CASCADE
    )
    SEX_CHOICES = (
        ('F', 'Female',),
        ('M', 'Male',)
    )
    code = models.CharField(max_length=255)
    sex = models.CharField(max_length=1,choices=SEX_CHOICES)
    reproduction_stage =  models.ForeignKey(ReproductionStage , on_delete=models.CASCADE)
    def __str__(self):
        return str(self.code)

class Birth(models.Model):
    pig_code = models.ForeignKey(Pig, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.datetime.now())
    live_born = models.IntegerField()
    stillbirth = models.IntegerField()
    def __str__(self):
        return str(self.pig_code)
